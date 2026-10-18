## ============================================================
## 字体配置（中文支持）
##
## Ren'Py common 代码将 style default 的字体硬编码为
## "DejaVuSans.ttf"（不含 CJK 字形）。gui.text_font 只对
## launcher 生成的 gui.rpy 模板生效，本项目未使用该模板，
## 因此用 config.font_replacement_map 在字体加载层做全局替换。
## NotoSansCJKsc 覆盖 中/日/韩 全部字形，后续日语配音项目名
## 显示无需再加字体。
## ============================================================

define config.font_replacement_map = {
    ("DejaVuSans.ttf", False, False): ("fonts/NotoSansCJKsc-Regular.otf", False, False),
    ("DejaVuSans.ttf", True,  False): ("fonts/NotoSansCJKsc-Regular.otf", True,  False),
    ("DejaVuSans.ttf", False, True):  ("fonts/NotoSansCJKsc-Regular.otf", False, True),
    ("DejaVuSans.ttf", True,  True):  ("fonts/NotoSansCJKsc-Regular.otf", True,  True),
}
