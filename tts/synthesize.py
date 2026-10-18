#!/usr/bin/env python3
# ============================================================
# whalegal TTS 批量合成
#
#   game/script/story_gen/*.rpy 里的 play_voice("v_xxx") 钩子
#     → 解析/校验（ID 算法: md5(角色显示名 + \x00 + 台词)[:12]）
#     → 按 tts/voices.py 的音线映射调用引擎
#     → ffmpeg 转 ogg → game/audio/voice/v_xxx.ogg
#
# 零第三方依赖（stdlib only）。增量合成：改哪行只重合成哪行。
#
# 用法:
#   python3 tts/synthesize.py                    # 全量增量合成（默认 dummy 引擎）
#   python3 tts/synthesize.py --list             # 只看合成计划
#   python3 tts/synthesize.py --check-only       # 只解析校验，不合成
#   python3 tts/synthesize.py --only v_80ae254d  # 按行ID前缀 / 台词片段过滤
#   python3 tts/synthesize.py --chapter ch01 --force
#   python3 tts/synthesize.py --engine sbv2      # 临时覆盖音线引擎
#   python3 tts/synthesize.py --prune            # 清理已无对应台词的音频
# ============================================================

import argparse
import glob
import hashlib
import json
import math
import os
import re
import shutil
import struct
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import wave

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from voices import VOICES, WHO_TO_VOICE, OVERRIDES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORY_GEN_DIR = os.path.join(ROOT, "game", "script", "story_gen")
JAPANESE_GEN_DIR = os.path.join(ROOT, "game", "tl", "japanese", "story_gen")
VOICE_DIR = os.path.join(ROOT, "game", "audio", "voice")
SPEAKERS_JSON = os.path.join(ROOT, "story", "speakers.json")
CACHE_JSON = os.path.join(ROOT, "tts", "cache.json")

RE_HOOK = re.compile(r'^\s*(?:\$ play_voice|voice voice_file)\("((?:[^"\\]|\\.)*)"\)\s*$')
RE_SAY = re.compile(r'^\s*([a-zA-Z_]\w*) "((?:[^"\\]|\\.)*)"(?: id [A-Za-z0-9_]+)?\s*$')

FFMPEG_ENC = {"ogg": ["-c:a", "libvorbis", "-q:a", "4"],
              "mp3": ["-c:a", "libmp3lame", "-q:a", "4"]}


# ---------------------------------------------------------------- 解析

def unescape(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            n = s[i + 1]
            out.append({"n": "\n", "t": "\t", '"': '"', "\\": "\\"}.get(n, "\\" + n))
            i += 2
        else:
            out.append(c)
            i += 1
    return "".join(out).replace("%%", "%").replace("[[", "[")


def parse_story_gen(errors, language="zh"):
    """返回 {v_id: (who, raw_text, relfile, lineno)}，并做完整性校验。"""
    lines_by_id = {}
    directory = JAPANESE_GEN_DIR if language == "jp" else STORY_GEN_DIR
    files = sorted(glob.glob(os.path.join(directory, "*.rpy")))
    if not files:
        errors.append("story_gen 目录为空: %s" % directory)
        return lines_by_id

    total_hooks = 0
    for fn in files:
        rel = os.path.relpath(fn, ROOT)
        with open(fn, encoding="utf-8") as f:
            rows = f.read().splitlines()
        pending = None
        for ln, raw in enumerate(rows, 1):
            m = RE_HOOK.match(raw)
            if m:
                total_hooks += 1
                if pending is not None:
                    errors.append("%s:%d 上一个钩子 %s 未配到台词" % (rel, ln, pending[0]))
                pending = (unescape(m.group(1)), rel, ln)
                continue
            m = RE_SAY.match(raw)
            if m:
                who, text = m.group(1), unescape(m.group(2))
                if pending is None:
                    continue  # narrator 等未挂钩台词，属正常
                vid, prel, pln = pending
                if who == "narrator":
                    errors.append("%s:%d 钩子 %s 配到了 narrator" % (prel, pln, vid))
                elif vid in lines_by_id and lines_by_id[vid][:2] != (who, text):
                    errors.append("行ID冲突 %s: %s vs %s"
                                  % (vid, lines_by_id[vid][:2], (who, text)))
                else:
                    lines_by_id[vid] = (who, text, rel, pln)
                pending = None
        if pending is not None:
            errors.append("%s 文件末尾钩子 %s 未配到台词" % (rel, pending[0]))

    # ID 复核（显示名哈希），story/speakers.json 缺失时跳过
    disp = {}
    if os.path.exists(SPEAKERS_JSON):
        try:
            with open(SPEAKERS_JSON, encoding="utf-8") as f:
                for d, v in json.load(f).items():
                    disp.setdefault(v, set()).add(d)
        except Exception as e:  # noqa: BLE001
            print("[warn] speakers.json 解析失败，跳过ID复核: %s" % e)
    for vid, (who, text, rel, pln) in lines_by_id.items():
        names = disp.get(who, set()) | {who}
        if not any("v_" + hashlib.md5((n + "\x00" + text).encode("utf-8")).hexdigest()[:12] == vid
                   for n in names):
            errors.append("%s:%d ID复核失败 %s（算法或文案与生成器不一致）" % (rel, pln, vid))
    return lines_by_id


def clean_text(text, interp_warn):
    t = re.sub(r"\{[^}]*\}", "", text)                 # renpy 文本标签
    for m in re.findall(r"\[[^\]]+\]", t):             # 插值
        interp_warn.add(m)
    t = re.sub(r"\[[^\]]+\]", "", t)
    return re.sub(r"\s+", " ", t).strip()


# ---------------------------------------------------------------- 引擎

def synth_dummy(text, params):
    sr = int(params.get("sample_rate", 22050))
    dur = max(0.4, min(30.0, 0.35 + 0.115 * len(text)))
    frames = struct.pack("<%dh" % int(sr * dur), *([0] * int(sr * dur)))
    import io
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(frames)
    return buf.getvalue()


def _http(req, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except Exception:  # noqa: BLE001
            if i == tries - 1:
                raise
            time.sleep(1.0 + i)


def synth_voicevox(text, params):
    url = params.get("url", "http://127.0.0.1:50021").rstrip("/")
    speaker = params.get("style_id", 3)
    q = urllib.parse.urlencode({"text": text, "speaker": speaker})
    query = json.loads(_http(urllib.request.Request(
        "%s/audio_query?%s" % (url, q), data=b"", method="POST")).decode("utf-8"))
    for k, v in params.items():          # speedScale/pitchScale 等透传
        if k not in ("url", "style_id"):
            query[k] = v
    body = json.dumps(query, ensure_ascii=False).encode("utf-8")
    return _http(urllib.request.Request(
        "%s/synthesis?%s" % (url, urllib.parse.urlencode({"speaker": speaker})),
        data=body, method="POST",
        headers={"Content-Type": "application/json"}))


def synth_sbv2(text, params):
    url = params.get("url", "http://127.0.0.1:5000").rstrip("/")
    p = {k: v for k, v in params.items() if k != "url"}
    p.setdefault("model_id", 0)
    p.setdefault("style", "Neutral")
    p["text"] = text
    p["language"] = {"zh": "ZH", "jp": "JP", "en": "EN"}.get(
        p.pop("lang", "jp"), "JP")
    return _http(urllib.request.Request(
        "%s/voice?%s" % (url, urllib.parse.urlencode(p))))


ENGINES = {"dummy": synth_dummy, "voicevox": synth_voicevox, "sbv2": synth_sbv2}


# ---------------------------------------------------------------- ffmpeg

def _ffmpeg_candidates():
    cands = []
    env = os.environ.get("WHALEGAL_FFMPEG")
    if env:
        cands.append(env)
    for pat in ("~/anaconda3/envs/*/lib/python*/site-packages/imageio_ffmpeg"
                "/binaries/ffmpeg-*linux*",  # imageio-ffmpeg 静态版（功能最全）
                "~/miniconda3/envs/*/lib/python*/site-packages/imageio_ffmpeg"
                "/binaries/ffmpeg-*linux*"):
        cands.extend(sorted(glob.glob(os.path.expanduser(pat)), reverse=True))
    w = shutil.which("ffmpeg")
    if w:
        cands.append(w)
    for pat in ("~/anaconda3/envs/*/bin/ffmpeg", "~/miniconda3/envs/*/bin/ffmpeg"):
        cands.extend(sorted(glob.glob(os.path.expanduser(pat)), reverse=True))
    return [c for c in cands if os.path.exists(c)]


def find_ffmpeg(fmt):
    """挑第一个具备目标格式编码器的 ffmpeg（探测一次并缓存）。"""
    need = {"ogg": "libvorbis", "mp3": "libmp3lame"}.get(fmt)
    for cand in _ffmpeg_candidates():
        if need:
            try:
                r = subprocess.run([cand, "-hide_banner", "-encoders"],
                                   capture_output=True, timeout=20)
                if need.encode() not in r.stdout:
                    continue
            except Exception:  # noqa: BLE001
                continue
        return cand
    return None


def convert(wav, out_path, fmt, ffmpeg):
    if fmt == "wav":
        with open(out_path, "wb") as f:
            f.write(wav)
        return
    tmp = out_path + ".tmp"
    with open(tmp, "wb") as f:
        r = subprocess.run([ffmpeg, "-y", "-loglevel", "error", "-f", "wav",
                            "-i", "pipe:0", "-f", fmt] + FFMPEG_ENC[fmt] + [tmp],
                           input=wav, capture_output=True)
    if r.returncode != 0:
        os.unlink(tmp)
        raise RuntimeError("ffmpeg: %s" % r.stderr.decode("utf-8", "replace")[-300:])
    os.replace(tmp, out_path)


# ---------------------------------------------------------------- 主流程

def main():
    ap = argparse.ArgumentParser(description="whalegal TTS 批量合成")
    ap.add_argument("--engine", choices=sorted(ENGINES), help="覆盖所有音线的引擎")
    ap.add_argument("--language", choices=["zh", "jp"], default="zh",
                    help="zh=中文主剧本；jp=已导入的日文翻译。两种语言使用独立音频目录与缓存")
    ap.add_argument("--format", choices=["ogg", "mp3", "wav"], default="ogg")
    ap.add_argument("--only", help="行ID前缀或台词片段过滤")
    ap.add_argument("--chapter", help="文件名子串过滤，如 ch01")
    ap.add_argument("--who", help="剧本角色过滤，如 cl")
    ap.add_argument("--voice", help="音线 key 过滤，如 claude")
    ap.add_argument("--force", action="store_true", help="忽略缓存全部重合成")
    ap.add_argument("--list", action="store_true", help="只打印合成计划")
    ap.add_argument("--check-only", action="store_true", help="只解析校验")
    ap.add_argument("--prune", action="store_true", help="删除已无对应台词的音频")
    ap.add_argument("--sleep", type=float, default=0.05, help="引擎请求间隔秒")
    args = ap.parse_args()

    global VOICE_DIR, CACHE_JSON
    if args.language == "jp":
        VOICE_DIR = os.path.join(ROOT, "game", "tl", "japanese", "audio", "voice")
        CACHE_JSON = os.path.join(ROOT, "tts", "cache-jp.json")

    errors = []
    lines = parse_story_gen(errors, args.language)
    print("解析 story_gen: %d 条钩子台词" % len(lines))
    if errors:
        for e in errors:
            print("[校验失败] %s" % e)
        if args.check_only or len(errors) > 5:
            sys.exit(1)

    # 过滤 + 音线解析
    interp_warn, work = set(), []
    unknown_who = {}
    for vid, (who, raw, rel, pln) in sorted(lines.items()):
        if args.chapter and args.chapter not in os.path.basename(rel):
            continue
        if args.only and args.only not in vid and args.only not in raw:
            continue
        if args.who and who != args.who:
            continue
        vkey = OVERRIDES.get(vid) or WHO_TO_VOICE.get(who)
        if vkey is None:
            unknown_who[who] = unknown_who.get(who, 0) + 1
            continue
        if args.voice and vkey != args.voice:
            continue
        cfg = dict(VOICES.get(vkey, {}))
        if not cfg:
            errors.append("音线 %s（%s）未在 tts/voices.py 定义" % (vkey, who))
            continue
        engine = args.engine or cfg.get("engine", "dummy")
        text = clean_text(raw, interp_warn)
        if text:
            work.append((vid, who, vkey, engine, cfg.get("params", {}),
                         args.language, text, rel, pln))
    if unknown_who:
        errors.append("未知角色（请在 tts/voices.py 的 WHO_TO_VOICE 补映射）: %s"
                      % unknown_who)
    if interp_warn:
        print("[warn] 台词含插值已剔除: %s" % sorted(interp_warn))
    if errors:
        for e in errors:
            print("[校验失败] %s" % e)
        sys.exit(1)

    per_voice = {}
    for _, _, vkey, _, _, _, _, _, _ in work:
        per_voice[vkey] = per_voice.get(vkey, 0) + 1
    print("合成计划: %d 条唯一音频 | %s" % (len(work),
          " ".join("%s=%d" % kv for kv in sorted(per_voice.items()))))
    if args.check_only:
        sys.exit(0)

    if args.list:
        for vid, who, vkey, engine, _, _, text, rel, pln in work:
            print("%s  %-9s -> %-9s [%s]  %s:%d  %s"
                  % (vid, who, vkey, engine, os.path.basename(rel), pln, text[:36]))
        sys.exit(0)

    # 缓存
    cache = {}
    if os.path.exists(CACHE_JSON) and not args.force:
        try:
            with open(CACHE_JSON, encoding="utf-8") as f:
                cache = json.load(f)
        except Exception:  # noqa: BLE001
            cache = {}

    ffmpeg = None
    if args.format != "wav":
        ffmpeg = find_ffmpeg(args.format)
        if not ffmpeg:
            print("[error] 找不到 ffmpeg（设 WHALEGAL_FFMPEG 或装到 PATH）")
            sys.exit(1)
        print("ffmpeg: %s" % ffmpeg)

    os.makedirs(VOICE_DIR, exist_ok=True)
    done = skipped = failed = 0
    failures = []
    for i, (vid, who, vkey, engine, params, lang, text, rel, pln) in enumerate(work):
        out_path = os.path.join(VOICE_DIR, "%s.%s" % (vid, args.format))
        h = hashlib.sha1(json.dumps(
            [vid, engine, vkey, params, lang, text, args.format],
            sort_keys=True).encode("utf-8")).hexdigest()
        if not args.force and cache.get(vid, {}).get("h") == h \
                and os.path.exists(out_path):
            skipped += 1
            continue
        ep = dict(params)
        if engine == "sbv2":
            ep["lang"] = lang
        t0 = time.time()
        try:
            wav = ENGINES[engine](text, ep)
            convert(wav, out_path, args.format, ffmpeg)
        except Exception as e:  # noqa: BLE001
            failed += 1
            failures.append((vid, "%s:%d" % (os.path.basename(rel), pln), str(e)))
            print("[fail] %s %s" % (vid, e))
            continue
        cache[vid] = {"h": h, "f": os.path.basename(out_path)}
        done += 1
        if done % 50 == 0 or i == len(work) - 1:
            print("  进度 %d/%d（新 %d 跳 %d 败 %d）" % (i + 1, len(work), done, skipped, failed))
        if args.sleep and engine != "dummy":
            time.sleep(args.sleep)

    with open(CACHE_JSON, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=1)

    # 清理孤儿音频
    if args.prune:
        # Keep voices used elsewhere in this language, even when --chapter/--only filters work.
        valid = set(lines)
        removed = 0
        for p in glob.glob(os.path.join(VOICE_DIR, "*.ogg")) + \
                 glob.glob(os.path.join(VOICE_DIR, "*.mp3")) + \
                 glob.glob(os.path.join(VOICE_DIR, "*.wav")):
            if os.path.splitext(os.path.basename(p))[0] not in valid:
                os.unlink(p)
                removed += 1
        print("清理孤儿音频: %d 个" % removed)

    print("=" * 46)
    print("完成: 新合成 %d | 缓存跳过 %d | 失败 %d" % (done, skipped, failed))
    for vid, loc, msg in failures:
        print("  失败 %s (%s): %s" % (vid, loc, msg))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
