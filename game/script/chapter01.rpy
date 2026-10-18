## ============================================================
## 第一章（冒烟测试剧本 —— 最小可玩流程）
## TODO: 正式沙雕文案导入 story/chapters/ 后替换
## ============================================================

label start:

    scene black

    narrator "这里是冒烟测试文本。如果你能看到这句话，说明引擎、剧本、打包、服务器四件套都活着。"

    s "哟！我是白鲸！这部 galgame 的主演兼饭桶担当！"

    k "我是小鲸……为什么我第一句话就要跟这么沙雕的家伙同台啊。"

    s "因为策划说：沙雕是第一生产力！"

    ## TODO: TTS 接入后启用 voice 语句
    ## voice "voice/ch01_0005.ogg"
    k "（叹气）好吧……总之，选一个吧。"

    menu:

        "选白鲸（果然还是沙雕一点好）":
            jump chapter01_whale

        "选小鲸（求你别这样）":
            jump chapter01_ko

label chapter01_whale:

    s "好耶！跟我走，带你去看世界上最大的饭桶——就是镜子里的你！"
    jump chapter01_end

label chapter01_ko:

    k "谢天谢地……终于不用一个人面对这家伙了。"
    jump chapter01_end

label chapter01_end:

    narrator "冒烟测试到此结束。Thank you for playing!"
    return
