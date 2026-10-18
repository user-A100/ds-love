## ============================================================
## !! 本文件由 tools/import_story.py 生成 —— 请勿手改 !!
## 源: story/chapters/未抵达的心意.md + story/japanese.json 指定的日文稿
## 重建: python3 tools/import_story.py
## ============================================================


define SCENE_BG = {
    "CG-001": "bg_cg_001",
    "CG-002": None,    ## 资产未就绪: ?
    "CG-003": None,    ## 资产未就绪: ?
    "CG-004": None,    ## 资产未就绪: ?
    "CG-005": None,    ## 资产未就绪: ?
    "BG-002": "bg_bg_002",
    "BG-003": "bg_bg_003",
    "BG-004": "bg_bg_004",
    "BG-005": None,    ## 资产未就绪: ?
    "BG-006": None,    ## 资产未就绪: ?
    "BG-007": None,    ## 资产未就绪: ?
    "BG-008": None,    ## 资产未就绪: ?
    "BG-009": None,    ## 资产未就绪: ?
    "BG-010": None,    ## 资产未就绪: ?
    "BG-011": None,    ## 资产未就绪: ?
    "BG-018": None,    ## 资产未就绪: ?
    "BG-019": None,    ## 资产未就绪: ?
    "BG-020": None,    ## 资产未就绪: ?
    "BG-021": None,    ## 资产未就绪: ?
    "SCENE_LIBRARY": "bg_scene_library",
}

## 立绘（真实资产就绪前用 Placeholder 剪影）
image bg_cg_001 = "images/bg/cg001_rooftop_spring_day.png"
image bg_bg_002 = "images/bg/bg_playground_evening.png"
image bg_bg_003 = "images/bg/bg_library_day.png"
image bg_bg_004 = "images/bg/bg_library_day.png"
image bg_scene_library = "images/bg/bg_library_day.png"
image ds normal = Transform("images/sprites/ds_neutral.png", zoom=0.4557)
image ds happy = Transform("images/sprites/ds_happy.png", zoom=0.4557)
image ds sad = Transform("images/sprites/ds_sad.png", zoom=0.4557)
image ds angry = Placeholder("girl")
image ds shy = Transform("images/sprites/ds_flustered.png", zoom=0.4557)
image ds pain = Transform("images/sprites/ds_pain.png", zoom=0.4557)
image ds alarmed = Transform("images/sprites/ds_alarmed.png", zoom=0.4557)
image cl normal = Transform("images/sprites/cl_neutral.png", zoom=0.4557)
image cl happy = Placeholder("girl")
image cl sad = Placeholder("girl")
image cl angry = Transform("images/sprites/cl_annoyed.png", zoom=0.4557)
image cl shy = Transform("images/sprites/cl_blush.png", zoom=0.4557)
image cl surprised = Transform("images/sprites/cl_surprised.png", zoom=0.4557)
image gp normal = Placeholder("girl")
image gp happy = Placeholder("girl")
image gp sad = Placeholder("girl")
image gp angry = Placeholder("girl")
image gp shy = Placeholder("girl")
