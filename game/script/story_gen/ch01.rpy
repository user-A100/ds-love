## ============================================================
## !! 本文件由 tools/import_story.py 生成 —— 请勿手改 !!
## 源: story/chapters/未抵达的心意.md (+ story/*.json)
## 重建: python3 tools/import_story.py
## ============================================================


label ch01:

    ## ── 场景: 第一章《认错的人》 ──

    ## ── 场景: 场景 1：寻找天台上的少女 ──
    $ scene_bg("BG-002")
    with trans_dissolve
    narrator "第二天，我开始寻找笔记本的主人。可是奇怪的是，学校里似乎没有多少人认识 DeepSeek。我只记得她蓝色的头发和那双明亮的眼睛。朋友听完我的描述，却给出了另一个名字。"
    $ play_voice("v_dba4cce52289")
    classmate "你说的该不会是 Claude 吧？"
    $ play_voice("v_8924030a4104")
    u "Claude？"
    $ play_voice("v_746ad4e09140")
    classmate "就是那个家里特别有钱的大小姐啊。听说她钢琴弹得特别好。"
    $ play_voice("v_9c9b85ad70af")
    u "可我记得她是蓝头发……"
    $ play_voice("v_d9d6c2adfa58")
    classmate "你看错了吧？学校里哪有那么多漂亮女生。"
    narrator "我半信半疑。直到放学后，在操场附近看到了 Claude。橙色长发，精致的发饰，干净整齐的制服。她身边似乎总有一种让人难以靠近的气场。"
    $ play_voice("v_80ae254d4021")
    show cl normal at sprite_pos_center with trans_dissolve
    cl "你从刚才开始就在看我吧？"
    $ play_voice("v_c84255281569")
    u "啊？"
    $ play_voice("v_a9afdfe7fc44")
    cl "有什么事就直说。偷偷摸摸的，很失礼。"
    $ play_voice("v_50a3b9ee358c")
    u "我只是想确认一件事。"
    $ play_voice("v_e70cd809a1fe")
    cl "确认什么？"
    $ play_voice("v_fd188758612d")
    u "你昨天是不是去过教学楼天台？"
    $ play_voice("v_766bdf29ed63")
    cl "哈？我为什么要去那种地方？"
    narrator "她皱起眉。"
    $ play_voice("v_d825f3832eca")
    cl "你该不会是想用这种老套的方式搭讪吧？"
    $ play_voice("v_0bdf1fd97cd4")
    u "不是，我——"
    $ play_voice("v_6eff9a22f220")
    cl "那就别挡路。"
    narrator "她转身离开。我看着她的背影，突然想起朋友的一句玩笑话。如果你真的喜欢她，就去单杠上做引体向上告白啊。也不知道哪根筋搭错了。"
    $ play_voice("v_d9e53fa8f82b")
    u "Claude！"
    narrator "她回过头。"
    $ play_voice("v_456d532bd390")
    cl "又怎么了？"
    $ play_voice("v_70a4665c0509")
    u "我有话想对你说！"
    narrator "我跑到操场旁的单杠前。握住横杆。努力将自己拉起来。"
    $ play_voice("v_f4ac22ed7248")
    u "请——"
    narrator "第二下。"
    $ play_voice("v_71b6bf0ee083")
    u "和我——"
    narrator "第三下。"
    $ play_voice("v_09122a559821")
    u "交往吧！！"
    narrator "整个操场安静了。Claude 呆呆地看着我。然后，她的脸一点点红了。"
    $ play_voice("v_3cd42841e4f6")
    cl "你、你是笨蛋吗？！"
    $ play_voice("v_ffd5904b0123")
    u "……可能是。"
    $ play_voice("v_aceda4de4b53")
    cl "哪有人会用这种方式告白的啊！"
    narrator "她别过脸。"
    $ play_voice("v_17ccc4c53cae")
    cl "而且我们根本不熟吧！"
    $ play_voice("v_181159f12195")
    u "所以……不行吗？"
    narrator "她沉默了好一会儿。"
    $ play_voice("v_a3fccccffe85")
    cl "……也不是完全不行。"
    $ play_voice("v_f7186d7cf129")
    u "诶？"
    $ play_voice("v_a3693795d1cc")
    cl "我说！可以先试着交往看看！"
    $ play_voice("v_0fcb28f81655")
    cl "但你别误会！只是觉得你这个人很奇怪，想看看你到底在想什么而已！"
    narrator "就这样。我因为一次认错人，莫名其妙地有了女朋友。而我真正想找的那个女孩——此刻正在另一栋教学楼里，翻遍自己的书包。"
    $ play_voice("v_445e39872668")
    show ds normal at sprite_pos_left with trans_dissolve
    ds "诶？笔记本呢？"
    $ play_voice("v_4a1d785dc144")
    ds "完蛋了完蛋了！我写了好久的故事啊！"

    ## ── 场景: 场景 2：笔记本的主人 ──
    hide cl
    hide ds
    $ scene_bg("BG-003")
    with trans_dissolve
    narrator "几天后，我终于在图书馆找到了 DeepSeek。她正趴在桌上，一脸绝望。"
    $ play_voice("v_4908a1855484")
    show ds normal at sprite_pos_left with trans_dissolve
    ds "呜……找不到了……"
    $ play_voice("v_a438ba4976e2")
    u "你是在找这个吗？"
    narrator "我把笔记本放在她面前。"
    $ play_voice("v_52a4ea9090e2")
    ds "啊啊啊！我的宝贝！！"
    narrator "她几乎跳了起来。"
    $ play_voice("v_3f2f7a971f16")
    ds "你是天台上的那个人！"
    $ play_voice("v_c20d97048b54")
    u "终于认出我了？"
    $ play_voice("v_b2098f6958a7")
    ds "当然记得！你是被我撞倒的那个！"
    $ play_voice("v_39af663c9170")
    u "……这个称呼能不能换一下？"
    narrator "她小心翼翼地接过笔记本。"
    $ play_voice("v_fc595934bbd6")
    u "里面写的是小说？"
    $ play_voice("v_72e96871249e")
    ds "嗯！虽然写得不太好啦……"
    $ play_voice("v_7cfb4c1f8028")
    u "我看了一点。"
    $ play_voice("v_9a8068fd217d")
    ds "诶？！"
    $ play_voice("v_e2ac63761268")
    u "我觉得很有意思。如果拍成电影的话，应该会很不错。"
    $ play_voice("v_32c649144e05")
    ds "真的吗？！"
    narrator "她一下子靠近。"
    $ play_voice("v_632b8fe2ea01")
    ds "你真的这么觉得？"
    $ play_voice("v_88c9b8aa98f4")
    u "嗯。"
    $ play_voice("v_f0bbd59c82d2")
    ds "那……那你愿意帮我拍出来吗？"
    narrator "那天，我第一次知道。这个看起来有些冒失、连自己的笔记本都能弄丢的女孩，竟然一直有一个创作故事的梦想。而她也第一次知道，我想成为电影导演。我们就这样约定了。她负责写故事。我负责把故事拍成电影。那时的我还不知道，这个约定会将我们的生活紧紧联系在一起。"

    ## ── 场景: 第一章（续）《写在笔记本里的约定》 ──
    hide ds

    ## ── 场景: 场景 3：第一次合作 ──
    $ scene_bg("BG-004")
    with trans_dissolve
    narrator "我原本以为，答应 DeepSeek 拍电影，只是一句随口说出的承诺。直到第二天下午，她抱着一大摞笔记本出现在我面前。"
    $ play_voice("v_6cb727cf5085")
    show ds normal at sprite_pos_left with trans_dissolve
    ds "锵锵！全部都带来了！"
    $ play_voice("v_8ad4a97d1e9f")
    u "……这是什么？"
    $ play_voice("v_b7da89aaad50")
    ds "剧本呀！"
    $ play_voice("v_3c35fce6d124")
    u "全部？"
    $ play_voice("v_a490e4fcfa21")
    ds "嗯！我昨天晚上把以前写的东西都整理了一遍！"
    $ play_voice("v_eba5b1bcb586")
    u "你昨天不是说只有一个故事吗？"
    $ play_voice("v_5eee3abe419e")
    ds "嘿嘿……写着写着就变多了。"
    narrator "我随手拿起最上面的一本。封面上画着一只歪歪扭扭的小鲸鱼。"
    $ play_voice("v_5d35411d3cf7")
    u "这是主角？"
    $ play_voice("v_737428143559")
    ds "嗯！它是一只想飞到天上的鲸鱼！"
    $ play_voice("v_59b296cbf09d")
    u "鲸鱼为什么要飞？"
    $ play_voice("v_f36ae76b941d")
    ds "因为它觉得，天上的星星可能也是大海呀。"
    $ play_voice("v_5f55f500d924")
    u "……"
    $ play_voice("v_05336fd63148")
    ds "很奇怪吗？"
    $ play_voice("v_9f7324bcacc0")
    u "不。我觉得挺好的。"
    $ play_voice("v_b5ca0b79526d")
    ds "真的？"
    $ play_voice("v_9e021948b332")
    u "真的。"
    narrator "她开心地笑起来。我翻开笔记本，继续往下读。故事的结构并不完整，许多地方甚至前后矛盾。但里面有一些画面，让我很想亲手拍出来。"
    $ play_voice("v_3fd11c0f9ddc")
    u "不过，光靠我们两个，恐怕拍不了电影。"
    $ play_voice("v_8a10fb6a7ccc")
    ds "诶？"
    $ play_voice("v_36370f2cc3ba")
    u "需要演员、摄影、道具，还需要有人帮忙修改剧本。"
    $ play_voice("v_ca0c6d502e66")
    ds "那怎么办？"
    $ play_voice("v_dfdc29c427c0")
    u "先去电影研究社看看吧。"
    $ play_voice("v_e0212af3b7bd")
    ds "好耶！"
    narrator "她突然站起来。"
    $ play_voice("v_7b22afff82d1")
    librarian "那边的同学，请保持安静！"
    $ play_voice("v_6d2fc91a46f0")
    ds "呜……对不起……"
    narrator "看着她低头道歉的样子，我突然觉得。和这个女孩一起拍电影，恐怕会发生很多意想不到的事情。不过，应该不会无聊。"

    jump ch02
