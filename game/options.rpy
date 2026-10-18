## ============================================================
## whalegal 构建配置
## ============================================================

define config.name = _("未抵达的心意")
define config.default_language = "japanese"
define gui.show_name = True
define gui.show_version = True
define gui.about = _p("""
《未抵达的心意》—— 校园恋爱视觉小说。
DeepSeek / Claude / GPT 与你之间的、未曾抵达的心意。
""")

define build.name = "whalegal"
define build.version = "0.1.0"

define config.version = "0.1.0"
define config.save_directory = "whalegal-1682947365"

## ------------------------------------------------------------
## 打包文件分类
## 文档: https://www.renpy.org/doc/html/build.html
## ------------------------------------------------------------

init python:

    ## 游戏本体（game/**）遵循 Ren'Py 默认分类：rpyc 进包、
    ## rpy 源码按 build.include_source 处理，无需手动干预。
    ## 这里只做“排除”与“文档”类覆盖。

    ## 工程文件不进分发包
    build.classify("docs/**", None)
    build.classify("story/**", None)
    build.classify("tts/**", None)
    build.classify("tools/**", None)
    build.classify("tests/**", None)
    build.classify("game/tests/**", None)
    build.classify("server/**", None)
    build.classify("lottery/**", None)
    build.classify("assets_src/**", None)
    build.classify("renpy-8.5.3-sdk/**", None)
    build.classify("renpy-*.tar.bz2", None)
    build.classify("dists/**", None)
    build.classify("game/saves/**", None)

    ## 空目录占位文件不进包
    build.classify("game/**/.keep", None)

    ## 瘦身：源码/缓存/文档不进分发包（game.zip 需低于 CF 25MiB 限制）
    build.include_source = False
    build.classify("game/cache/**", None)
    build.classify("**.md", None)
    build.classify("story/**", None)

    ## Android/iOS 暂不支持
    build.include_android = False
    build.include_ios = False

    build.documentation = "README.md"


## Project title theme; scene music is generated from story/art_direction.json.
define config.main_menu_music = "audio/bgm/titile_theme.mp3"
