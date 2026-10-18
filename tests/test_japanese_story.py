import importlib.util
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from import_story import Importer, esc
from story_text import Event, align_chapter, parse_markdown

spec = importlib.util.spec_from_file_location('synthesize', ROOT / 'tts/synthesize.py')
tts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tts)


class JapaneseStoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.importer = Importer()
        cls.importer.parse()

    def test_all_units_have_unique_native_translations(self):
        files = self.importer.render()
        original = '\n'.join(v for k, v in files.items() if not k.startswith('tl/'))
        translated = '\n'.join(v for k, v in files.items() if k.startswith('tl/'))
        ids = re.findall(r' id (story_\w+)$', original, re.M)
        targets = re.findall(r'^translate japanese (story_\w+):$', translated, re.M)
        self.assertEqual(len(ids), 3950)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertCountEqual(ids, targets)

    def test_generated_files_are_current(self):
        for name, expected in self.importer.render().items():
            path = ROOT / 'game' / name if name.startswith('tl/') else ROOT / 'game/script/story_gen' / name
            self.assertEqual(path.read_text(encoding='utf-8'), expected, name)

    def test_both_locale_voice_ids_match_their_dialogue(self):
        for language in ('zh', 'jp'):
            errors = []
            voices = tts.parse_story_gen(errors, language)
            self.assertFalse(errors, errors)
            self.assertGreater(len(voices), 1000)

    def test_multiline_and_literal_escaping_round_trip(self):
        text = '手紙\n100% [name] "引用" \\n'
        encoded = esc(text)
        self.assertNotIn('\n', encoded)
        self.assertEqual(tts.unescape(encoded), text)

    def test_parser_preserves_letter_and_narrative_paragraphs(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'script.md'
            path.write_text('# 設定\nこれは本文ではない\n## 場面\n一段目。\n\n二段目。\nファイル名は：\n**GPT：**\n「一行目\n\n二行目」\n', encoding='utf-8')
            says = [e for e in parse_markdown(path, 'ch00') if e.kind == 'say']
        self.assertEqual([e.speaker for e in says], ['narrator'] * 3 + ['GPT'])
        self.assertEqual(says[-1].text, '一行目\n二行目')

    def test_alignment_rejects_wrong_speaker_or_location(self):
        zh = [Event('heading', 'ch00', 'scene'), Event('say', 'ch00', '原文', 'User')]
        wrong_speaker = [Event('heading', 'ch00', 'scene'), Event('say', 'ch00', '訳', 'GPT')]
        wrong_location = [Event('say', 'ch00', '訳', 'User')]
        for ja in (wrong_speaker, wrong_location):
            with self.assertRaises(ValueError):
                align_chapter(zh, ja, 'ch00', {'User': 'u', 'GPT': 'gp'})


if __name__ == '__main__':
    unittest.main()
