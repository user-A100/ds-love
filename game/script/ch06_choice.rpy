## ============================================================
## 第六章（场景 6-01 ~ 6-05：最后的期限 / 选择的代价）
## 6-05 为路线分歧点：→ route_ds / route_cl / route_gp
## 源文本: story/chapters/未抵达的心意.md（约 L6863-7300）
## 状态: 骨架占位（DS 线已有完整剧本，CL/GP 线待补）
## ============================================================

label ch06:

    scene black with trans_fade
    narrator "（第六章占位）最后的期限……"

    ds "这一次，换我来找你，可以吗？"
    cl "……真是的，到最后还要让我等。"
    gp "答案，就藏在你一直没说出口的话里。"

    menu:
        "追向 DeepSeek":
            jump route_ds
        "（Claude 线 · 待剧本）":
            jump route_cl
        "（GPT 线 · 待剧本）":
            jump route_gp
