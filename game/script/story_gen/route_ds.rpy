## ============================================================
## !! 本文件由 tools/import_story.py 生成 —— 请勿手改 !!
## 源: story/chapters/未抵达的心意.md + story/japanese.json 指定的日文稿
## 重建: python3 tools/import_story.py
## ============================================================


label route_ds:

    ## ── 场景: 场景 DS-01｜最初的约定 ──
    ## 演出: 时间：一月二十七日 · 夜晚 · DeepSeek 的大学
    ## 演出: 旁白
    play music "audio/bgm/bgm_deepseek.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-01 · 第一次主动说想见她
    scene art_act06_bg29_crossing_sunset with trans_dissolve
    narrator "铁路道口的栏杆缓缓升起。" id story_route_ds_1af411488f38_1
    narrator "人群从我身边走过。" id story_route_ds_e9b4ba411031_1
    narrator "我却仍然站在原地。" id story_route_ds_5e345721d52a_1
    narrator "手机屏幕上，停留着三个熟悉的名字。" id story_route_ds_ca484cf6014e_1
    narrator "Claude。" id story_route_ds_e3d485db693f_1
    narrator "GPT。" id story_route_ds_8d7c4cc4ca40_1
    narrator "DeepSeek。" id story_route_ds_7c0be0110e83_1
    narrator "我想起了三年前的那个下午。" id story_route_ds_791c16c61625_1
    narrator "教学楼天台。" id story_route_ds_9ad72a310bbf_1
    narrator "从矮墙上跌落的蓝发少女。" id story_route_ds_4f2c5817ac0e_1
    show art_act01_pr01_blue_notebook as story_prop at story_prop_pos with trans_dissolve
    narrator "还有那本被遗忘在地上的笔记本。" id story_route_ds_296396a3b116_1
    narrator "如果那天我没有去天台。" id story_route_ds_fbcb6b98a326_1
    narrator "如果她没有弄丢笔记本。" id story_route_ds_b92e251b58fb_1
    narrator "如果我没有读到她写下的故事。" id story_route_ds_35e111469987_1
    hide story_prop with trans_dissolve
    narrator "我们大概就不会相遇。" id story_route_ds_d6ad7769993e_1
    narrator "可后来发生的一切，让我明白了一件事。" id story_route_ds_5bed914a02f7_1
    narrator "我想拍电影，不只是因为喜欢镜头里的世界。" id story_route_ds_51d6ce47764c_1
    narrator "也是因为有一个人，总是迫不及待地想把自己看到的世界讲给我听。" id story_route_ds_46e0407cdadb_1
    ## 演出: 旁白
    narrator "我打开 DeepSeek 的聊天窗口。" id story_route_ds_e925a43d1ee5_1
    voice voice_file("v_ccad2eb99aee")
    u "你现在在哪里？" id story_route_ds_ccad2eb99aee_1
    narrator "过了几秒。" id story_route_ds_2628bf9e2337_1
    voice voice_file("v_9a8068fd217d")
    ds "诶？！" id story_route_ds_9a8068fd217d_1
    voice voice_file("v_7dddda9d1eee")
    ds "我在活动室呀！" id story_route_ds_7dddda9d1eee_1
    voice voice_file("v_f95cb4a58628")
    ds "怎么啦？是不是我的剧本有问题？" id story_route_ds_f95cb4a58628_1
    voice voice_file("v_64555b5aeaf3")
    u "没有。" id story_route_ds_64555b5aeaf3_1
    voice voice_file("v_175b2b140b85")
    u "我想见你。" id story_route_ds_175b2b140b85_1
    narrator "聊天窗口突然安静下来。" id story_route_ds_dcd56a1a5475_1
    narrator "过了很久。" id story_route_ds_96a5b53f2f55_1
    voice voice_file("v_1675b3f39da6")
    ds "……现在？" id story_route_ds_1675b3f39da6_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_1
    voice voice_file("v_2d68bf31ba10")
    ds "可是已经很晚了哦？" id story_route_ds_2d68bf31ba10_1
    voice voice_file("v_7b0d860cefd7")
    u "我知道。" id story_route_ds_7b0d860cefd7_1
    voice voice_file("v_841643c7ab45")
    ds "那、那你过来吧！" id story_route_ds_841643c7ab45_1
    voice voice_file("v_d912804f7cc7")
    ds "我等你！" id story_route_ds_d912804f7cc7_1
    ## 演出: 旁白
    scene art_ds_route_bg30_university_night with trans_dissolve
    narrator "我收起手机，向车站跑去。" id story_route_ds_4cabec1034ac_1
    narrator "这是第一次。" id story_route_ds_1d9f103d4221_1
    narrator "不是因为电影。" id story_route_ds_83854d26c230_1
    narrator "不是因为剧本。" id story_route_ds_74e819a61585_1
    narrator "也不是因为她需要我帮忙。" id story_route_ds_d07cbd95327c_1
    narrator "而是因为我想见她。" id story_route_ds_79a698a31863_1

    ## ── 场景: 场景 DS-02｜迟来的回答 ──
    ## 演出: 时间：同日 · 晚上 21:10 · 电影研究社
    ## 演出: 旁白
    play music "audio/bgm/bgm_deepseek.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-02 · 先说喜欢，再承担过去
    scene art_ds_route_bg26_filmclub_night with trans_dissolve
    narrator "我赶到活动室时，DeepSeek 正趴在桌上写东西。" id story_route_ds_69c00c9344c1_1
    narrator "听见开门声，她猛地抬起头。" id story_route_ds_92bcf1802616_1
    voice voice_file("v_51a5ecf1d639")
    ds "User！" id story_route_ds_51a5ecf1d639_1
    voice voice_file("v_b18d06d72c2b")
    ds "你怎么真的来了呀！" id story_route_ds_b18d06d72c2b_1
    voice voice_file("v_46e3f6d4e8f6")
    u "不是你说会等我吗？" id story_route_ds_46e3f6d4e8f6_1
    voice voice_file("v_827d30dcbdfb")
    ds "是、是这样没错啦……" id story_route_ds_827d30dcbdfb_1
    narrator "她慌忙把桌上的稿纸整理好。" id story_route_ds_10a8ab638156_1
    voice voice_file("v_c24bcaa60dc1")
    ds "所以……有什么事吗？" id story_route_ds_c24bcaa60dc1_1
    narrator "我走到她面前。" id story_route_ds_a7da6107f6fb_1
    voice voice_file("v_c5f965228eed")
    u "DeepSeek。" id story_route_ds_c5f965228eed_1
    voice voice_file("v_0e748d627265")
    ds "嗯？" id story_route_ds_0e748d627265_1
    voice voice_file("v_02580165cce5")
    u "还记得水族馆那天，你对我说的话吗？" id story_route_ds_02580165cce5_1
    narrator "她的动作停住了。" id story_route_ds_56cacd79acf0_1
    voice voice_file("v_0b5c4ac47fce")
    ds "……记得。" id story_route_ds_0b5c4ac47fce_1
    voice voice_file("v_560f4e2d48ea")
    u "你说你喜欢我。" id story_route_ds_560f4e2d48ea_1
    voice voice_file("v_f3620bb93bd0")
    ds "嗯。" id story_route_ds_f3620bb93bd0_1
    narrator "她低下头。" id story_route_ds_00d82bb20a31_1
    voice voice_file("v_cc89cc8ec4fd")
    ds "不过我不是说过了吗，你不用勉强自己回答。" id story_route_ds_cc89cc8ec4fd_1
    voice voice_file("v_7b0d860cefd7")
    u "我知道。" id story_route_ds_7b0d860cefd7_2
    voice voice_file("v_cb08364174a8")
    u "但我不想再让你等了。" id story_route_ds_cb08364174a8_1
    narrator "她慢慢抬起头。" id story_route_ds_6b481e818485_1
    voice voice_file("v_beb8abdad9de")
    u "我喜欢你。" id story_route_ds_beb8abdad9de_1
    ## 演出: 旁白
    narrator "DeepSeek 呆住了。" id story_route_ds_b90632f70a29_1
    narrator "几秒过去。" id story_route_ds_1043c66b46b0_1
    narrator "她仍然没有说话。" id story_route_ds_4607927c123b_1
    voice voice_file("v_a013bb8e4345")
    u "DeepSeek？" id story_route_ds_a013bb8e4345_1
    voice voice_file("v_7cace157f7b3")
    ds "……诶？" id story_route_ds_7cace157f7b3_1
    voice voice_file("v_a2fdfe083814")
    u "我说，我喜欢你。" id story_route_ds_a2fdfe083814_1
    voice voice_file("v_21792d23be56")
    ds "等、等等！" id story_route_ds_21792d23be56_1
    narrator "她突然向后退了一步。" id story_route_ds_95d9c98885dc_1
    voice voice_file("v_9b3c015274ea")
    ds "你是不是又在开玩笑？！" id story_route_ds_9b3c015274ea_1
    voice voice_file("v_64555b5aeaf3")
    u "没有。" id story_route_ds_64555b5aeaf3_2
    voice voice_file("v_aa52563715bf")
    ds "真的？！" id story_route_ds_aa52563715bf_1
    voice voice_file("v_9e021948b332")
    u "真的。" id story_route_ds_9e021948b332_1
    voice voice_file("v_8470fad9af29")
    ds "可、可是……" id story_route_ds_8470fad9af29_1
    narrator "她低下头，声音渐渐小了下去。" id story_route_ds_bbfb965fce63_1
    voice voice_file("v_ae9fc0c16126")
    ds "Claude 呢？" id story_route_ds_ae9fc0c16126_1
    voice voice_file("v_bb0c60ee5890")
    ds "GPT 学姐呢？" id story_route_ds_bb0c60ee5890_1
    ## 演出: 旁白
    narrator "我没有立刻回答。" id story_route_ds_5a5d42383828_1
    narrator "因为她问到了我一直无法回避的问题。" id story_route_ds_77b579af9d4f_1
    voice voice_file("v_d0a64b0fc041")
    u "我会和她们说清楚。" id story_route_ds_d0a64b0fc041_1
    voice voice_file("v_a1c733c19657")
    ds "……" id story_route_ds_a1c733c19657_1
    voice voice_file("v_4388e6509e0d")
    u "尤其是 Claude。我们之间还有很多事情没有解决。" id story_route_ds_4388e6509e0d_1
    voice voice_file("v_63103f24e796")
    u "我不应该在没有结束那段关系之前，就要求你成为我的恋人。" id story_route_ds_63103f24e796_1
    narrator "DeepSeek 看着我。" id story_route_ds_79b3cc6b0b80_1
    voice voice_file("v_609ea61dbdfd")
    ds "那……你现在为什么要告诉我？" id story_route_ds_609ea61dbdfd_1
    voice voice_file("v_a9563ad4a036")
    u "因为我不想再让你误以为，自己只能一直等待。" id story_route_ds_a9563ad4a036_1
    show art_act01_pr01_blue_notebook as story_prop at story_prop_pos with trans_dissolve
    narrator "我把她交给我保管的旧笔记本放在桌上。" id story_route_ds_3ed8bce3256d_1
    voice voice_file("v_6a0931beefe1")
    u "我想继续和你一起拍电影。" id story_route_ds_6a0931beefe1_1
    voice voice_file("v_baf37099d56b")
    u "也想在不拍电影的时候，和你待在一起。" id story_route_ds_baf37099d56b_1
    voice voice_file("v_51ec94aebbfc")
    u "但我需要先把过去的事情处理好。" id story_route_ds_51ec94aebbfc_1
    hide story_prop with trans_dissolve
    narrator "她低下头。" id story_route_ds_00d82bb20a31_2
    narrator "过了很久，轻轻点了点头。" id story_route_ds_6b994711e19b_1
    voice voice_file("v_1a79727e0e23")
    ds "……好。" id story_route_ds_1a79727e0e23_1
    voice voice_file("v_e12697886f15")
    ds "那我等你把事情说清楚。" id story_route_ds_e12697886f15_1
    narrator "她又急忙补充。" id story_route_ds_3c6c055aed5e_1
    voice voice_file("v_769aa2e9e3e8")
    ds "不、不过不是以前那种一直等下去哦！" id story_route_ds_769aa2e9e3e8_1
    voice voice_file("v_19370dff71bc")
    ds "这次我也有自己的事情要做！" id story_route_ds_19370dff71bc_1
    voice voice_file("v_7b0d860cefd7")
    u "我知道。" id story_route_ds_7b0d860cefd7_3
    voice voice_file("v_810606352b8b")
    ds "而且……" id story_route_ds_810606352b8b_1
    narrator "她看着我，眼睛慢慢红了。" id story_route_ds_834ea3c3d5ee_1
    voice voice_file("v_8bdf8c9475f8")
    ds "如果你最后还是改变主意，我真的会生气的。" id story_route_ds_8bdf8c9475f8_1
    voice voice_file("v_8ba68d990031")
    u "不会了。" id story_route_ds_8ba68d990031_1
    ## 演出: 旁白
    narrator "她没有扑进我的怀里。" id story_route_ds_1239b44914fc_1
    narrator "也没有立刻接受这场迟来的告白。" id story_route_ds_f3a899fbfc68_1
    narrator "只是把那本笔记本重新推到我面前。" id story_route_ds_42b47ed7aa5e_1
    voice voice_file("v_f8ddde1cb7b9")
    ds "那就等你真正准备好了，再还给我吧。" id story_route_ds_f8ddde1cb7b9_1

    ## ── 场景: 场景 DS-03｜与过去告别 ──
    ## 演出: 时间：一月二十八日 · 音乐厅
    ## 演出: 旁白
    play music "audio/bgm/bgm_claude.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-03 · 对Claude说清楚
    scene art_ds_route_bg20_rehearsal_evening with trans_dissolve
    narrator "第二天下午，我去找了 Claude。" id story_route_ds_c27408a6cf5a_1
    show art_act06_pr09_music_document_case as story_prop at story_prop_pos with trans_dissolve
    narrator "她正在整理即将带回欧洲的乐谱。" id story_route_ds_d62880713652_1
    narrator "看见我，她似乎已经猜到了什么。" id story_route_ds_b3afa652da08_1
    show art_act05_claude_indoor_neutral as cl at sprite_pos_center with trans_dissolve
    voice voice_file("v_219648a88e1f")
    cl "……你来了。" id story_route_ds_219648a88e1f_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_2
    hide story_prop with trans_dissolve
    voice voice_file("v_42b0121679ba")
    cl "想好了吗？" id story_route_ds_42b0121679ba_1
    voice voice_file("v_2d1df85a91c3")
    u "想好了。" id story_route_ds_2d1df85a91c3_1
    narrator "她放下手里的乐谱。" id story_route_ds_603de0ef0518_1
    voice voice_file("v_fba36e018adb")
    cl "那就说吧。" id story_route_ds_fba36e018adb_1
    ## 演出: 旁白
    narrator "我看着她。" id story_route_ds_e2f5aab3b666_1
    narrator "那个曾经因为我荒唐的告白而成为我女朋友的少女。" id story_route_ds_08e8556bb0c0_1
    narrator "那个在音乐教室里陪我练习吉他的人。" id story_route_ds_1f352d68b94b_1
    narrator "那个明明喜欢着我，却独自去了欧洲的女孩。" id story_route_ds_e611424c3f95_1
    narrator "我知道，接下来的话会伤害她。" id story_route_ds_e5b60edc89f5_1
    narrator "可如果继续沉默，只会让她受到更深的伤害。" id story_route_ds_c2ce7ff25a63_1
    voice voice_file("v_674763ce4358")
    u "Claude。" id story_route_ds_674763ce4358_1
    voice voice_file("v_4c658b378563")
    u "对不起。" id story_route_ds_4c658b378563_1
    show art_ds_route_claude_indoor_hurt as cl at sprite_pos_center with trans_dissolve
    narrator "她的表情微微一变。" id story_route_ds_4075a43fbbfc_1
    voice voice_file("v_d6bb00ebdcec")
    cl "……" id story_route_ds_d6bb00ebdcec_1
    voice voice_file("v_48b2119c5ad8")
    u "我喜欢上了 DeepSeek。" id story_route_ds_48b2119c5ad8_1
    ## 演出: 旁白
    narrator "房间里安静下来。" id story_route_ds_a8d829f318a0_1
    narrator "Claude 没有立刻回答。" id story_route_ds_ebdb9a5440df_1
    narrator "她只是看着我。" id story_route_ds_2cf1583c6c12_1
    narrator "过了很久，才轻轻笑了一声。" id story_route_ds_14ce1ddec78b_1
    voice voice_file("v_b905ec04a325")
    cl "……原来如此。" id story_route_ds_b905ec04a325_1
    voice voice_file("v_8f2f09cd6d64")
    cl "是那个蓝头发的笨蛋啊。" id story_route_ds_8f2f09cd6d64_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_3
    voice voice_file("v_d2c7f770bf2b")
    cl "从什么时候开始的？" id story_route_ds_d2c7f770bf2b_1
    voice voice_file("v_18748ed01b74")
    u "我也说不清楚。" id story_route_ds_18748ed01b74_1
    voice voice_file("v_1ef434dc0e8a")
    u "也许很早以前就开始了，只是我一直没有认真面对。" id story_route_ds_1ef434dc0e8a_1
    narrator "她低下头。" id story_route_ds_00d82bb20a31_3
    voice voice_file("v_c3c8b5fc705b")
    cl "真过分啊。" id story_route_ds_c3c8b5fc705b_1
    voice voice_file("v_5f55f500d924")
    u "……" id story_route_ds_5f55f500d924_1
    voice voice_file("v_7a28d63508c5")
    cl "明明当初先告白的人是你。" id story_route_ds_7a28d63508c5_1
    voice voice_file("v_ab0cf7451c5e")
    cl "让我以为自己被喜欢着的人，也是你。" id story_route_ds_ab0cf7451c5e_1
    voice voice_file("v_0023249fd152")
    cl "结果最后，还是你先喜欢上了别人。" id story_route_ds_0023249fd152_1
    ## 演出: 旁白
    narrator "我没有辩解。" id story_route_ds_5fe76d668b33_1
    narrator "Claude 走到钢琴前。" id story_route_ds_9ff4f2bf335b_1
    narrator "轻轻按下一个琴键。" id story_route_ds_d9b7b10f6895_1
    voice voice_file("v_e6cb50ab6211")
    cl "你知道吗？" id story_route_ds_e6cb50ab6211_1
    voice voice_file("v_bdc896a2804b")
    cl "我在欧洲的时候，真的想过很多次。" id story_route_ds_bdc896a2804b_1
    voice voice_file("v_a4998cebf53c")
    cl "如果当初没有答应你的告白，会不会更好。" id story_route_ds_a4998cebf53c_1
    narrator "她的声音开始颤抖。" id story_route_ds_68c32f9ad8e7_1
    voice voice_file("v_f490351953aa")
    cl "如果我们只是普通朋友，我是不是就不会这么难过。" id story_route_ds_f490351953aa_1
    voice voice_file("v_5f55f500d924")
    u "……" id story_route_ds_5f55f500d924_2
    voice voice_file("v_93805b3e6c4a")
    cl "可是后来，我又觉得。" id story_route_ds_93805b3e6c4a_1
    voice voice_file("v_38c481b47c43")
    cl "如果没有遇见你，我大概也不会知道，原来自己会这么喜欢一个人。" id story_route_ds_38c481b47c43_1
    narrator "她抬起头。" id story_route_ds_54b76a6e010c_1
    show art_ds_route_claude_indoor_cry as cl at sprite_pos_center with trans_dissolve
    narrator "眼角已经泛红。" id story_route_ds_e88609512837_1
    voice voice_file("v_48fd27972b3b")
    cl "所以我不后悔。" id story_route_ds_48fd27972b3b_1
    voice voice_file("v_5f24f4547826")
    cl "只是……" id story_route_ds_5f24f4547826_1
    narrator "她用手背擦了擦眼睛。" id story_route_ds_e5218e826a0b_1
    voice voice_file("v_882e67c9daef")
    cl "真的很不甘心。" id story_route_ds_882e67c9daef_1
    ## 演出: 旁白
    narrator "我站在原地。" id story_route_ds_d9745483a730_1
    narrator "不知道该说些什么。" id story_route_ds_71835617ffbc_1
    narrator "Claude 深吸了一口气。" id story_route_ds_3412e19b1593_1
    show art_ds_route_claude_indoor_firm as cl at sprite_pos_center with trans_dissolve
    voice voice_file("v_b7522895c724")
    cl "你走吧。" id story_route_ds_b7522895c724_1
    voice voice_file("v_a3533d81ade5")
    u "Claude……" id story_route_ds_a3533d81ade5_1
    voice voice_file("v_95a1227a7744")
    cl "我说，你走吧。" id story_route_ds_95a1227a7744_1
    voice voice_file("v_6691149391bc")
    cl "再待下去，我可能会说出一些很难听的话。" id story_route_ds_6691149391bc_1
    narrator "我轻轻点头。" id story_route_ds_ebd464839f04_1
    narrator "走到门口时，她突然叫住我。" id story_route_ds_99cbad7da431_1
    voice voice_file("v_98dac76185b9")
    cl "User。" id story_route_ds_98dac76185b9_1
    voice voice_file("v_7235f2204469")
    u "嗯？" id story_route_ds_7235f2204469_1
    voice voice_file("v_cb3443205781")
    cl "既然已经决定了，就不要再伤害她。" id story_route_ds_cb3443205781_1
    voice voice_file("v_06637ed97d1a")
    cl "也不要再回来问我，自己是不是选错了。" id story_route_ds_06637ed97d1a_1
    ## 演出: 旁白
    narrator "我没有回头。" id story_route_ds_df74889bd9ac_1
    voice voice_file("v_6ef6a0065c21")
    u "……我知道。" id story_route_ds_6ef6a0065c21_1
    ## 演出: 音效 关门声。
    ## 演出: 旁白
    hide cl with trans_dissolve
    narrator "门关上的瞬间，音乐教室里重新响起钢琴声。" id story_route_ds_f6fcf8572628_1
    narrator "是那首我们曾经一起演奏的歌。" id story_route_ds_4b974c7fb433_1
    narrator "《届かない恋》。" id story_route_ds_62eaaa5379c9_1
    narrator "可这一次，只有她一个人在弹。" id story_route_ds_d81e45851e99_1

    ## ── 场景: 场景 DS-04｜学姐的祝福 ──
    ## 演出: 时间：一月二十九日 · 出版社附近的咖啡馆
    ## 演出: 旁白
    play music "audio/bgm/bgm_gpt.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-04 · 祝福里也有她的难过
    scene art_act05_bg23_cafe_snow_day with trans_dissolve
    narrator "与 Claude 告别后的第二天，我去见了 GPT 学姐。" id story_route_ds_0f238db840a2_1
    narrator "她已经知道我要来。" id story_route_ds_ec88963a22f9_1
    narrator "桌上放着两杯热茶。" id story_route_ds_208c263661f3_1
    show art_act05_gpt_work_neutral as gp at sprite_pos_right with trans_dissolve
    voice voice_file("v_7b4ac0e6e9e6")
    gp "坐吧。" id story_route_ds_7b4ac0e6e9e6_1
    voice voice_file("v_b82850ddc78e")
    u "学姐。" id story_route_ds_b82850ddc78e_1
    voice voice_file("v_4705eb82ff56")
    gp "嗯？" id story_route_ds_4705eb82ff56_1
    voice voice_file("v_11fddc44d4fa")
    u "我想告诉你一件事。" id story_route_ds_11fddc44d4fa_1
    narrator "她看着我。" id story_route_ds_d18d9ba31bef_1
    narrator "随后轻轻点头。" id story_route_ds_d27afce268c1_1
    voice voice_file("v_643d258ae304")
    gp "我在听。" id story_route_ds_643d258ae304_1
    voice voice_file("v_96c01a55ff32")
    u "我决定和 DeepSeek 在一起。" id story_route_ds_96c01a55ff32_1
    ## 演出: 旁白
    narrator "她端起茶杯的手停了一下。" id story_route_ds_d3832ffaa740_1
    narrator "但很快，又恢复了平静。" id story_route_ds_4cd5b7176218_1
    voice voice_file("v_48a81b0b5b18")
    gp "……这样啊。" id story_route_ds_48a81b0b5b18_1
    voice voice_file("v_4c658b378563")
    u "对不起。" id story_route_ds_4c658b378563_2
    voice voice_file("v_9acdd6059780")
    gp "为什么要道歉呢？" id story_route_ds_9acdd6059780_1
    voice voice_file("v_edf74a9d91e1")
    u "因为我知道，你一直……" id story_route_ds_edf74a9d91e1_1
    voice voice_file("v_8e5d6be8f73c")
    gp "User。" id story_route_ds_8e5d6be8f73c_1
    narrator "她轻轻打断我。" id story_route_ds_a555e78a9472_1
    voice voice_file("v_7b71b314cf95")
    gp "我以前就说过。" id story_route_ds_7b71b314cf95_1
    voice voice_file("v_0cd26affa188")
    gp "我帮助你，不是为了让你以后选择我。" id story_route_ds_0cd26affa188_1
    ## 演出: 旁白
    narrator "她微笑着看向我。" id story_route_ds_5074426dac82_1
    voice voice_file("v_50f5e652671f")
    gp "你终于能够认真面对自己的感情，我其实很高兴。" id story_route_ds_50f5e652671f_1
    voice voice_file("v_5f55f500d924")
    u "……" id story_route_ds_5f55f500d924_3
    show art_ds_route_gpt_work_lonely as gp at sprite_pos_right with trans_dissolve
    voice voice_file("v_37bdbca6e251")
    gp "虽然，稍微有一点难过就是了。" id story_route_ds_37bdbca6e251_1
    narrator "这是她第一次在我面前如此坦率地承认自己的失落。" id story_route_ds_affa321a2bfd_1
    voice voice_file("v_d805e6fefca1")
    gp "不过没关系。" id story_route_ds_d805e6fefca1_1
    voice voice_file("v_0f6e8b9aab77")
    gp "我还有自己的工作，还有很多想做的事情。" id story_route_ds_0f6e8b9aab77_1
    voice voice_file("v_d5f1e4240d8b")
    gp "而且……" id story_route_ds_d5f1e4240d8b_1
    narrator "她停顿了一下。" id story_route_ds_deaf7e779ad2_1
    voice voice_file("v_73483ecc44cd")
    gp "DeepSeek 是个很好的女孩。" id story_route_ds_73483ecc44cd_1
    voice voice_file("v_7eacae0cdf17")
    gp "她真的很喜欢你。" id story_route_ds_7eacae0cdf17_1
    ## 演出: 旁白
    narrator "我低下头。" id story_route_ds_46f115285034_1
    voice voice_file("v_646f22cd76cf")
    u "谢谢你，学姐。" id story_route_ds_646f22cd76cf_1
    voice voice_file("v_c4bf00b654de")
    gp "又说谢谢。" id story_route_ds_c4bf00b654de_1
    show art_act05_gpt_work_neutral as gp at sprite_pos_right with trans_dissolve
    narrator "她笑了。" id story_route_ds_56298f1f1ffb_1
    voice voice_file("v_46343c5cb3dc")
    gp "你总是这样。" id story_route_ds_46343c5cb3dc_1
    voice voice_file("v_0fd8f6d2c21f")
    gp "不过，这次我就收下了。" id story_route_ds_0fd8f6d2c21f_1
    ## 演出: 旁白
    show art_act06_pr21_interview_portfolio as story_prop at story_prop_pos with trans_dissolve
    narrator "离开前，她把作品集资料递给我。" id story_route_ds_4bb53fd13341_1
    voice voice_file("v_daa0a1fbb398")
    gp "项目面试的结果应该很快就会出来。" id story_route_ds_daa0a1fbb398_1
    voice voice_file("v_5abf92550e17")
    gp "不管感情上发生什么，都不要忘记自己的梦想。" id story_route_ds_5abf92550e17_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_4
    hide story_prop with trans_dissolve
    voice voice_file("v_145ddaafdcdb")
    gp "还有。" id story_route_ds_145ddaafdcdb_1
    voice voice_file("v_4bc7badb508b")
    u "什么？" id story_route_ds_4bc7badb508b_1
    voice voice_file("v_623e0fd60ac1")
    gp "以后如果真的拍出一部很棒的电影，记得邀请我去看。" id story_route_ds_623e0fd60ac1_1
    voice voice_file("v_611d2bbd2a67")
    u "一定。" id story_route_ds_611d2bbd2a67_1
    ## 演出: 旁白
    narrator "她挥了挥手。" id story_route_ds_66cd2629ebbe_1
    hide gp with trans_dissolve
    narrator "我走出咖啡馆。" id story_route_ds_d026886c3633_1
    narrator "回头时，透过玻璃窗，看见她仍然坐在原来的位置。" id story_route_ds_905bbb83f050_1
    narrator "她没有看向我。" id story_route_ds_98a04af08479_1
    narrator "只是低着头，安静地喝着已经有些凉了的茶。" id story_route_ds_36967acf8395_1

    ## ── 场景: 场景 DS-05｜第二次告白 ──
    ## 演出: 时间：一月三十日 · 公园 · 黄昏
    ## 演出: 旁白
    play music "audio/bgm/bgm_deepseek.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-05 · 这次可以成为恋人了
    scene art_act04_bg_lakeside_sunset with trans_dissolve
    narrator "我约 DeepSeek 在上次去过的公园见面。" id story_route_ds_243b0c67b94e_1
    narrator "这里距离水族馆不远。" id story_route_ds_c41899156b98_1
    narrator "几个月前，她就是在这里第一次向我告白。" id story_route_ds_63107f6477f7_1
    narrator "那时候，她紧张得连话都说不完整。" id story_route_ds_174f0ec69ef5_1
    narrator "而我没有给她答案。" id story_route_ds_e9659f4c0873_1
    narrator "今天，我比约定时间提前到了半个小时。" id story_route_ds_68c6717f2afd_1
    narrator "可当我走进公园时，却发现她已经站在那里。" id story_route_ds_e0c5e94e488a_1
    voice voice_file("v_5a38a955886a")
    u "你怎么来这么早？" id story_route_ds_5a38a955886a_1
    show art_act05_ds_win_neutral as ds at sprite_pos_left with trans_dissolve
    voice voice_file("v_a7782c7ec24c")
    ds "嘿嘿。" id story_route_ds_a7782c7ec24c_1
    voice voice_file("v_7322ea330424")
    ds "因为有点期待嘛。" id story_route_ds_7322ea330424_1
    narrator "她抬起头。" id story_route_ds_54b76a6e010c_2
    voice voice_file("v_862278267c2d")
    ds "怎么样？" id story_route_ds_862278267c2d_1
    voice voice_file("v_88db329a046c")
    u "我已经和 Claude、GPT 学姐说清楚了。" id story_route_ds_88db329a046c_1
    narrator "她的笑容慢慢消失。" id story_route_ds_4cd8c0aeace7_1
    voice voice_file("v_290e218b9aad")
    ds "……真的？" id story_route_ds_290e218b9aad_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_5
    voice voice_file("v_e1674012e694")
    ds "她们……还好吗？" id story_route_ds_e1674012e694_1
    voice voice_file("v_1575f49bd4b9")
    u "我想，她们需要一点时间。" id story_route_ds_1575f49bd4b9_1
    narrator "她低下头。" id story_route_ds_00d82bb20a31_4
    voice voice_file("v_9624080bebd0")
    ds "这样啊。" id story_route_ds_9624080bebd0_1
    ## 演出: 旁白
    narrator "我走到她面前。" id story_route_ds_a7da6107f6fb_2
    voice voice_file("v_c5f965228eed")
    u "DeepSeek。" id story_route_ds_c5f965228eed_2
    voice voice_file("v_0e748d627265")
    ds "嗯？" id story_route_ds_0e748d627265_2
    voice voice_file("v_beb8abdad9de")
    u "我喜欢你。" id story_route_ds_beb8abdad9de_2
    voice voice_file("v_38d5771ffaa2")
    u "这一次，不是因为误会，也不是因为害怕失去。" id story_route_ds_38d5771ffaa2_1
    voice voice_file("v_0c81e79effc1")
    u "我想和你一起继续生活。" id story_route_ds_0c81e79effc1_1
    voice voice_file("v_e12a09644305")
    u "一起拍电影，一起讨论剧本。" id story_route_ds_e12a09644305_1
    voice voice_file("v_d875ed24ac25")
    u "也想和你一起经历那些和电影无关的普通日子。" id story_route_ds_d875ed24ac25_1
    narrator "她呆呆地看着我。" id story_route_ds_f4f17ad79515_1
    narrator "眼泪突然落了下来。" id story_route_ds_d0a700703104_1
    voice voice_file("v_2803f44edf18")
    ds "……笨蛋。" id story_route_ds_2803f44edf18_1
    voice voice_file("v_7235f2204469")
    u "嗯？" id story_route_ds_7235f2204469_2
    voice voice_file("v_792580a3c141")
    ds "你真的好笨啊！" id story_route_ds_792580a3c141_1
    narrator "她一边哭，一边笑。" id story_route_ds_160e29f41bc1_1
    voice voice_file("v_e6b864d4eb99")
    ds "为什么非要让我等这么久！" id story_route_ds_e6b864d4eb99_1
    voice voice_file("v_4c658b378563")
    u "对不起。" id story_route_ds_4c658b378563_3
    voice voice_file("v_7d77370aa904")
    ds "不许道歉！" id story_route_ds_7d77370aa904_1
    voice voice_file("v_e4076e818a83")
    ds "这种时候应该说别的话吧！" id story_route_ds_e4076e818a83_1
    narrator "我忍不住笑了。" id story_route_ds_d316041b00d7_1
    voice voice_file("v_3fa9082d00fd")
    u "那……" id story_route_ds_3fa9082d00fd_1
    voice voice_file("v_7b087555a2e3")
    u "请和我交往吧。" id story_route_ds_7b087555a2e3_1
    narrator "她用力点头。" id story_route_ds_4241cd1dac76_1
    voice voice_file("v_57cd12ae7731")
    ds "嗯！" id story_route_ds_57cd12ae7731_1
    voice voice_file("v_d35286ffffd3")
    ds "我愿意！" id story_route_ds_d35286ffffd3_1
    ## 演出: 旁白
    narrator "她扑进我的怀里。" id story_route_ds_6c148f2e99c9_1
    narrator "我轻轻抱住她。" id story_route_ds_9d9a38f60ef8_1
    narrator "远处的夕阳落在湖面上。" id story_route_ds_fe13f8eef10f_1
    narrator "那一瞬间，我忽然想起很多年前。" id story_route_ds_ec0b5e538ff7_1
    narrator "天台上，那个从矮墙上跌落的蓝发少女。" id story_route_ds_cb41c79e2fd5_1
    narrator "她当时一边揉着额头，一边认真地问我。" id story_route_ds_d7dac1308b23_1
    narrator "「有趣……是在夸我吗？」" id story_route_ds_783252439239_1
    narrator "那时候，我怎么也不会想到。" id story_route_ds_c223bce91f62_1
    narrator "多年以后，我会在这里，抱着同一个女孩。" id story_route_ds_43a72947383a_1
    ## 演出: CG：DeepSeek 与 User 在夕阳下拥抱

    ## ── 场景: 场景 DS-06｜梦想与爱情之间 ──
    ## 演出: 时间：两个月后 · 春天
    ## 演出: 旁白
    play music "audio/bgm/bgm_farewell.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-06 · 终于得到的机会也意味着远行
    scene art_ds_route_bg26_filmclub_spring_day with trans_dissolve
    narrator "和 DeepSeek 正式交往以后，我们的生活并没有立刻发生翻天覆地的变化。" id story_route_ds_327d63ebad15_1
    narrator "她依然经常忘记带东西。" id story_route_ds_a4e9755e097a_1
    narrator "依然会因为突然想到一个故事情节，就在半夜给我发消息。" id story_route_ds_d764efa4a8eb_1
    narrator "也依然会在讨论剧本时，因为意见不同而和我争论。" id story_route_ds_900c0e4fe58d_1
    narrator "只是现在，她会在放学后主动牵住我的手。" id story_route_ds_5165bdccdfd0_1
    narrator "也会在分别时，红着脸问我明天能不能再见面。" id story_route_ds_63d21edd95b0_1
    voice voice_file("v_51a5ecf1d639")
    ds "User！" id story_route_ds_51a5ecf1d639_2
    voice voice_file("v_8517678f9232")
    u "怎么了？" id story_route_ds_8517678f9232_1
    voice voice_file("v_7cd82d918799")
    ds "我有个超级重要的消息！" id story_route_ds_7cd82d918799_1
    voice voice_file("v_39cfb3e6bc12")
    u "你的小说又写完了？" id story_route_ds_39cfb3e6bc12_1
    voice voice_file("v_d658e01fc19c")
    ds "不是啦！" id story_route_ds_d658e01fc19c_1
    narrator "她把手机递给我。" id story_route_ds_9b21bd6c572b_1
    narrator "屏幕上，是一家出版社发来的通知。" id story_route_ds_db79faaa2dcc_1
    narrator "她投稿的小说通过了初步审核。" id story_route_ds_e278cbfae30d_1
    narrator "出版社邀请她参加一项长期创作计划。" id story_route_ds_624e24dff739_1
    voice voice_file("v_3b5d25ea110f")
    u "这是好事啊！" id story_route_ds_3b5d25ea110f_1
    voice voice_file("v_57cd12ae7731")
    ds "嗯！" id story_route_ds_57cd12ae7731_2

    ## ── 场景: 场景 DS-06｜梦想与爱情之间（续） ──
    ## 演出: 旁白
    narrator "她投稿的小说通过了初步审核。" id story_route_ds_e278cbfae30d_2
    narrator "出版社邀请她参加一项长期创作计划。" id story_route_ds_624e24dff739_2
    voice voice_file("v_3b5d25ea110f")
    u "这是好事啊！" id story_route_ds_3b5d25ea110f_2
    voice voice_file("v_57cd12ae7731")
    ds "嗯！" id story_route_ds_57cd12ae7731_3
    narrator "她兴奋地点了点头。" id story_route_ds_72b798e3dc61_1
    narrator "可没过多久，脸上的笑容又渐渐消失了。" id story_route_ds_2bf87a862203_1
    voice voice_file("v_8517678f9232")
    u "怎么了？" id story_route_ds_8517678f9232_2
    voice voice_file("v_fcf13f24dea5")
    ds "就是……" id story_route_ds_fcf13f24dea5_1
    narrator "她低下头，轻轻捏着衣角。" id story_route_ds_3563760fad60_1
    voice voice_file("v_34bd10277cb9")
    ds "那个创作计划，要去法国。" id story_route_ds_34bd10277cb9_1
    voice voice_file("v_0f1ce36ea9bf")
    u "法国？" id story_route_ds_0f1ce36ea9bf_1
    voice voice_file("v_cc59513c5e61")
    ds "嗯。出版社说可以在那里接受培训，还能接触到很多优秀的创作者。" id story_route_ds_cc59513c5e61_1
    voice voice_file("v_58f87fefd6f6")
    ds "而且……可能要待好几年。" id story_route_ds_58f87fefd6f6_1
    ## 演出: 旁白
    narrator "我愣了一下。" id story_route_ds_975feb05c0bc_1
    narrator "法国。" id story_route_ds_7bce30dfc66c_1
    narrator "这个遥远的国家，曾经因为 Claude 而在我的生活里留下了太多回忆。" id story_route_ds_f45abee63bff_1
    narrator "现在，DeepSeek 也即将前往那里。" id story_route_ds_1f936fa2d86b_1
    voice voice_file("v_e55be3e4de6a")
    u "你想去吗？" id story_route_ds_e55be3e4de6a_1
    narrator "她沉默了一会儿。" id story_route_ds_13ac6da729c8_1
    voice voice_file("v_4e6e2b15ab2a")
    ds "想。" id story_route_ds_4e6e2b15ab2a_1
    narrator "回答得很轻，却没有犹豫。" id story_route_ds_66aee661896d_1
    voice voice_file("v_5b256e0a3a25")
    ds "我真的很想去。" id story_route_ds_5b256e0a3a25_1
    voice voice_file("v_0ff2e0065462")
    ds "以前我总觉得，只要能和你一起拍电影就好了。" id story_route_ds_0ff2e0065462_1
    voice voice_file("v_4329f5f130ad")
    ds "可是后来，我发现自己还有好多好多故事想写。" id story_route_ds_4329f5f130ad_1
    voice voice_file("v_90a6c077daf8")
    ds "我想成为真正的作家。" id story_route_ds_90a6c077daf8_1
    narrator "她抬起头。" id story_route_ds_54b76a6e010c_3
    voice voice_file("v_6c2c0ed9139e")
    ds "可是……" id story_route_ds_6c2c0ed9139e_1
    voice voice_file("v_c4b1fd254d7d")
    u "可是？" id story_route_ds_c4b1fd254d7d_1
    voice voice_file("v_ae08c76b5fb2")
    ds "我们才刚刚在一起呀。" id story_route_ds_ae08c76b5fb2_1
    ## 演出: 旁白
    narrator "她的眼睛有些红。" id story_route_ds_21518d0a263d_1
    voice voice_file("v_be47b8d71996")
    ds "明明等了那么久。" id story_route_ds_be47b8d71996_1
    voice voice_file("v_cc01fe2e2ce9")
    ds "好不容易才听到你说喜欢我。" id story_route_ds_cc01fe2e2ce9_1
    voice voice_file("v_7a1b5ce8aa7b")
    ds "结果现在，又要分开了。" id story_route_ds_7a1b5ce8aa7b_1
    narrator "她努力笑了一下。" id story_route_ds_126d83d342a9_1
    voice voice_file("v_f41c1becf5fd")
    ds "是不是很笨呀？" id story_route_ds_f41c1becf5fd_1
    voice voice_file("v_8505b9a1f6a9")
    u "不笨。" id story_route_ds_8505b9a1f6a9_1
    voice voice_file("v_b5ca0b79526d")
    ds "真的？" id story_route_ds_b5ca0b79526d_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_6
    narrator "我轻轻握住她的手。" id story_route_ds_ef0f9fc7f4cf_1
    voice voice_file("v_9f0844ba4abc")
    u "你以前不是说过吗？" id story_route_ds_9f0844ba4abc_1
    voice voice_file("v_561e4d5c5b8c")
    u "就算最后没有和喜欢的人在一起，也不能放弃自己想做的事情。" id story_route_ds_561e4d5c5b8c_1
    voice voice_file("v_a1c733c19657")
    ds "……" id story_route_ds_a1c733c19657_2
    voice voice_file("v_fe28f8f0411c")
    u "我喜欢的 DeepSeek，是那个会为了写出一个好故事，熬夜改十几遍剧本的女孩。" id story_route_ds_fe28f8f0411c_1
    voice voice_file("v_b90254d16bc7")
    u "不是那个为了陪在我身边，放弃自己梦想的人。" id story_route_ds_b90254d16bc7_1
    narrator "她低下头。" id story_route_ds_00d82bb20a31_5
    narrator "眼泪一滴滴落在我们的手背上。" id story_route_ds_56c0bb47402c_1
    voice voice_file("v_ba04d2f649df")
    ds "……你这样说，我会更舍不得的。" id story_route_ds_ba04d2f649df_1

    ## ── 场景: 场景 DS-07｜回到原点 ──
    ## 演出: 时间：DeepSeek 出国前一周 · 傍晚
    ## 演出: 旁白
    play music "audio/bgm/bgm_deepseek.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-07 · 回到天台订下新约定
    scene art_act04_bg_rooftop_evening with trans_dissolve
    narrator "距离 DeepSeek 离开还有一个星期。" id story_route_ds_e19ed6b8fb04_1
    narrator "那天，我们去了高中母校。" id story_route_ds_4db9f54843be_1
    narrator "学校正好放假，校园里几乎没有人。" id story_route_ds_628fdafd1580_1
    narrator "我们沿着熟悉的走廊，慢慢走向教学楼顶层。" id story_route_ds_76c27f9f2ce2_1
    voice voice_file("v_cad9abeaf55a")
    ds "哇！这里一点都没变！" id story_route_ds_cad9abeaf55a_1
    narrator "她推开天台的门。" id story_route_ds_03e9207a355e_1
    narrator "春天的风迎面吹来。" id story_route_ds_29517e87364b_1
    narrator "远处的樱花已经盛开。" id story_route_ds_e618e3bbae21_1
    voice voice_file("v_8d6148f8b05d")
    ds "User！你看！" id story_route_ds_8d6148f8b05d_1
    narrator "她跑到当年那面矮墙旁。" id story_route_ds_9f9f05470a88_1
    voice voice_file("v_fe58f10f4fd7")
    u "别再爬上去了。" id story_route_ds_fe58f10f4fd7_1
    voice voice_file("v_c2f9ecaa0ded")
    ds "诶？为什么！" id story_route_ds_c2f9ecaa0ded_1
    voice voice_file("v_6550f20bc8d1")
    u "你忘了第一次见面的时候，差点把我撞倒？" id story_route_ds_6550f20bc8d1_1
    voice voice_file("v_a92e06d50f1d")
    ds "才不是差点！明明已经撞倒了！" id story_route_ds_a92e06d50f1d_1
    voice voice_file("v_a3a92aa08d4a")
    u "……你还挺骄傲。" id story_route_ds_a3a92aa08d4a_1
    narrator "她笑了起来。" id story_route_ds_716fb1e444a4_1
    show art_act01_pr01_blue_notebook as story_prop at story_prop_pos with trans_dissolve
    narrator "过了一会儿，她从书包里拿出一本浅蓝色的笔记本。" id story_route_ds_aa4164d97925_1
    voice voice_file("v_6313fa8d7786")
    ds "锵锵！" id story_route_ds_6313fa8d7786_1
    voice voice_file("v_dfda618868ac")
    u "这不是……" id story_route_ds_dfda618868ac_1
    voice voice_file("v_01e6c280abc1")
    ds "嗯！最开始的那本！" id story_route_ds_01e6c280abc1_1
    narrator "她轻轻翻开。" id story_route_ds_0a6d0c2e9d2f_1
    narrator "第一页写着那些稚嫩的故事。" id story_route_ds_9f36e168c3ef_1
    narrator "有些地方还画着歪歪扭扭的插图。" id story_route_ds_a4dbed4a2401_1
    voice voice_file("v_9a8a117e4cf3")
    ds "那时候，我连一个完整的故事都写不好。" id story_route_ds_9a8a117e4cf3_1
    voice voice_file("v_56afde833126")
    ds "可是你却说，想把它拍成电影。" id story_route_ds_56afde833126_1
    voice voice_file("v_814934455c37")
    u "我记得。" id story_route_ds_814934455c37_1
    voice voice_file("v_9c7b607e71f0")
    ds "所以我一直觉得，自己一定要写出一部真正厉害的作品。" id story_route_ds_9c7b607e71f0_1
    narrator "她把笔记本递给我。" id story_route_ds_2ffa583f4dc1_1
    voice voice_file("v_4b28eef60716")
    ds "这个，再交给你一次。" id story_route_ds_4b28eef60716_1
    hide story_prop with trans_dissolve
    voice voice_file("v_5fe64f8c35c7")
    u "为什么？" id story_route_ds_5fe64f8c35c7_1
    voice voice_file("v_a5a7f5ef5236")
    ds "因为我想和你做一个新的约定。" id story_route_ds_a5a7f5ef5236_1
    narrator "她深吸一口气。" id story_route_ds_d2237cb6690c_1
    voice voice_file("v_4ec57b6be064")
    ds "等我从法国回来，你要把我的小说拍成电影！" id story_route_ds_4ec57b6be064_1
    voice voice_file("v_333e949d441c")
    u "好。" id story_route_ds_333e949d441c_1
    voice voice_file("v_49719a0cedf6")
    ds "不许敷衍！" id story_route_ds_49719a0cedf6_1
    voice voice_file("v_5516e8e65179")
    u "我保证。" id story_route_ds_5516e8e65179_1
    voice voice_file("v_b44c8044d5c0")
    ds "而且还要拍得特别特别好！" id story_route_ds_b44c8044d5c0_1
    voice voice_file("v_f6daec4760ca")
    u "要求真多啊。" id story_route_ds_f6daec4760ca_1
    voice voice_file("v_a7782c7ec24c")
    ds "嘿嘿。" id story_route_ds_a7782c7ec24c_2
    narrator "她伸出小指。" id story_route_ds_7dda7c87c5eb_1
    voice voice_file("v_bb89a78e2dfe")
    ds "拉钩！" id story_route_ds_bb89a78e2dfe_1
    narrator "我轻轻勾住她的小指。" id story_route_ds_0d57912ebd89_1
    ## 演出: 旁白
    narrator "很多年前，我们也是在这里相遇。" id story_route_ds_462ff90fe633_1
    narrator "那时候，我们还不知道彼此的名字。" id story_route_ds_c87291da149f_1
    narrator "不知道未来会发生什么。" id story_route_ds_6038165f72c0_1
    narrator "更不知道有一天，我们会站在同一个地方，认真讨论分别之后的生活。" id story_route_ds_7d3b8537dfbd_1
    voice voice_file("v_0a84887f827d")
    ds "User。" id story_route_ds_0a84887f827d_1
    voice voice_file("v_7235f2204469")
    u "嗯？" id story_route_ds_7235f2204469_3
    voice voice_file("v_14f1cb8e0c15")
    ds "我真的很喜欢你。" id story_route_ds_14f1cb8e0c15_1
    voice voice_file("v_6e2b02165d38")
    u "我也是。" id story_route_ds_6e2b02165d38_1
    narrator "她靠在我的肩膀上。" id story_route_ds_0cf3741f30be_1
    voice voice_file("v_41653d8d77cd")
    ds "那就不要忘记我哦。" id story_route_ds_41653d8d77cd_1

    ## ── 场景: 场景 DS-08｜暂时分开 ──
    ## 演出: 时间：出国前三天 · 公园
    ## 演出: 旁白
    play music "audio/bgm/bgm_farewell.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-08 · 你有没有问过我想怎样
    scene art_ds_route_bg17_lakeside_spring_overcast with trans_dissolve
    narrator "DeepSeek 离开的前三天，我主动提出，希望我们暂时把恋人的关系放回原点。" id story_route_ds_1293af1a667b_1
    narrator "她愣住了。" id story_route_ds_be2b60c9df15_1
    voice voice_file("v_7cace157f7b3")
    ds "……诶？" id story_route_ds_7cace157f7b3_2
    voice voice_file("v_22b3acd6c18f")
    u "我想了很久。" id story_route_ds_22b3acd6c18f_1
    voice voice_file("v_c845ab7e3945")
    u "你接下来要去法国，认真学习写作。" id story_route_ds_c845ab7e3945_1
    voice voice_file("v_7cda3d56bce9")
    u "我也要继续积累拍摄经验，争取真正成为导演。" id story_route_ds_7cda3d56bce9_1
    voice voice_file("v_a8b8c30293f1")
    u "如果我们一直因为见不到面而难过，最后可能谁都没办法好好追逐自己的梦想。" id story_route_ds_a8b8c30293f1_1
    narrator "她低下头。" id story_route_ds_00d82bb20a31_6
    voice voice_file("v_58d102077fd7")
    ds "所以……你想分手吗？" id story_route_ds_58d102077fd7_1
    voice voice_file("v_9a3a9cae8a7d")
    u "不是因为不喜欢你。" id story_route_ds_9a3a9cae8a7d_1
    voice voice_file("v_1e713411c8f1")
    u "而是我想等我们都能真正独立地生活以后，再认真面对未来。" id story_route_ds_1e713411c8f1_1
    ## 演出: 旁白
    narrator "她没有立刻回答。" id story_route_ds_803d9b503f9c_1
    narrator "过了很久，才轻轻开口。" id story_route_ds_65f1f929686b_1
    voice voice_file("v_870b8aaa4924")
    ds "……你知道吗？" id story_route_ds_870b8aaa4924_1
    voice voice_file("v_900e5004da07")
    ds "我其实很讨厌你总是替别人做决定。" id story_route_ds_900e5004da07_1
    narrator "我怔住了。" id story_route_ds_341e1cf3e04f_1
    voice voice_file("v_528911dc9acf")
    ds "以前也是。" id story_route_ds_528911dc9acf_1
    voice voice_file("v_72c45120dec7")
    ds "你觉得不回答我，是为了不让我难过。" id story_route_ds_72c45120dec7_1
    voice voice_file("v_d638909c5c1c")
    ds "现在又觉得，暂时分开是为了让我好好写作。" id story_route_ds_d638909c5c1c_1
    narrator "她抬起头。" id story_route_ds_54b76a6e010c_4
    narrator "眼睛里已经有了泪光。" id story_route_ds_444ecdd6fe32_1
    voice voice_file("v_a9352001c7f5")
    ds "可是你有没有问过，我到底想怎么样？" id story_route_ds_a9352001c7f5_1
    ## 演出: 旁白
    narrator "我没有回答。" id story_route_ds_3045611bcabc_1
    narrator "她轻轻擦了擦眼角。" id story_route_ds_fbd3cbe381f2_1
    voice voice_file("v_60285fdbf518")
    ds "我也会舍不得。" id story_route_ds_60285fdbf518_1
    voice voice_file("v_ee8c4627e289")
    ds "也会想每天和你说话。" id story_route_ds_ee8c4627e289_1
    voice voice_file("v_75d171ced7e1")
    ds "可是我又不是小孩子了。" id story_route_ds_75d171ced7e1_1
    voice voice_file("v_d5627c86dad6")
    ds "我可以自己决定要不要去法国，也可以自己决定要不要继续喜欢你。" id story_route_ds_d5627c86dad6_1
    narrator "她看着我。" id story_route_ds_d18d9ba31bef_2
    voice voice_file("v_1b1e0bcbd65e")
    ds "不过……" id story_route_ds_1b1e0bcbd65e_1
    narrator "她的声音渐渐低下来。" id story_route_ds_2d5ad6d2e252_1
    voice voice_file("v_b11c9ed0b4f3")
    ds "我也明白，你想说什么。" id story_route_ds_b11c9ed0b4f3_1
    voice voice_file("v_dc3916789540")
    ds "我们都还有很长的路要走。" id story_route_ds_dc3916789540_1
    voice voice_file("v_4ee3b57d7e2f")
    ds "如果一直把未来寄托在一个约定上，可能真的会很辛苦。" id story_route_ds_4ee3b57d7e2f_1
    ## 演出: 旁白
    narrator "那天，我们谈了很久。" id story_route_ds_249e78a4bec4_1
    narrator "最后，决定暂时结束恋人关系。" id story_route_ds_9a60f518d3df_1
    narrator "不是因为不再喜欢。" id story_route_ds_6f1194d12d98_1
    narrator "而是因为我们都希望，下一次站在彼此面前时，能够更加坚定地选择对方。" id story_route_ds_e718650f3d4d_1
    voice voice_file("v_7252c6ef74a2")
    ds "那说好了。" id story_route_ds_7252c6ef74a2_1
    voice voice_file("v_7235f2204469")
    u "嗯？" id story_route_ds_7235f2204469_4
    voice voice_file("v_80a1260a6b3d")
    ds "以后如果又遇见了，你可不许因为觉得亏欠我，就说喜欢我。" id story_route_ds_80a1260a6b3d_1
    voice voice_file("v_f6dec558dda2")
    ds "要是真的喜欢，才能说哦！" id story_route_ds_f6dec558dda2_1
    voice voice_file("v_333e949d441c")
    u "好。" id story_route_ds_333e949d441c_2
    narrator "她笑了。" id story_route_ds_56298f1f1ffb_2
    narrator "眼泪却还在不停往下掉。" id story_route_ds_208fc0886851_1

    ## ── 场景: 场景 DS-09｜机场的告别 ──
    ## 演出: 时间：四月 · 国际机场
    ## 演出: 旁白
    play music "audio/bgm/bgm_farewell.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-09 · 带着想飞的鲸鱼出发
    scene art_act04_bg_airport_depart_day with trans_dissolve
    narrator "DeepSeek 离开的那天，天气很好。" id story_route_ds_4922dcab521e_1
    show art_act04_pr14_suitcase as story_prop at story_prop_pos with trans_dissolve
    narrator "我陪她办理登机手续。" id story_route_ds_3319ba7a3758_1
    narrator "她的行李箱上挂着一只蓝色的小鲸鱼。" id story_route_ds_bb31704992c2_1
    narrator "是她自己买的。" id story_route_ds_a01165f1bc19_1
    voice voice_file("v_0fe8961cb56b")
    u "这个是什么？" id story_route_ds_0fe8961cb56b_1
    hide story_prop with trans_dissolve
    voice voice_file("v_af22d3fe051b")
    ds "护身符！" id story_route_ds_af22d3fe051b_1
    voice voice_file("v_d3cce29bab38")
    u "鲸鱼？" id story_route_ds_d3cce29bab38_1
    voice voice_file("v_57cd12ae7731")
    ds "嗯！" id story_route_ds_57cd12ae7731_4
    voice voice_file("v_bd9ab5f41f79")
    ds "你忘啦？我以前写过一只想飞到天上的鲸鱼。" id story_route_ds_bd9ab5f41f79_1
    voice voice_file("v_05a3d59649dc")
    u "记得。" id story_route_ds_05a3d59649dc_1
    voice voice_file("v_f72a49bc01ce")
    ds "所以我想带着它一起去看看更大的世界。" id story_route_ds_f72a49bc01ce_1
    ## 演出: 旁白
    narrator "广播里响起登机通知。" id story_route_ds_3204fbff56be_1
    narrator "DeepSeek 看了看时间。" id story_route_ds_f177546d3240_1
    voice voice_file("v_aa312048d080")
    ds "……该走了。" id story_route_ds_aa312048d080_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_7
    narrator "她拉起行李箱。" id story_route_ds_5b2f5c61af47_1
    narrator "走了两步，又突然转过身。" id story_route_ds_a19456989936_1
    voice voice_file("v_51a5ecf1d639")
    ds "User！" id story_route_ds_51a5ecf1d639_3
    voice voice_file("v_8517678f9232")
    u "怎么了？" id story_route_ds_8517678f9232_3
    narrator "她跑回来，用力抱住我。" id story_route_ds_24e5f3c64906_1
    voice voice_file("v_baa51f9f0510")
    ds "我一定会成为很厉害的作家的！" id story_route_ds_baa51f9f0510_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_8
    voice voice_file("v_a98f0293cc8c")
    ds "你也一定要成为导演！" id story_route_ds_a98f0293cc8c_1
    voice voice_file("v_333e949d441c")
    u "好。" id story_route_ds_333e949d441c_3
    voice voice_file("v_0f9f7c08082a")
    ds "然后……" id story_route_ds_0f9f7c08082a_1
    narrator "她停顿了一下。" id story_route_ds_deaf7e779ad2_2
    voice voice_file("v_1ebc55fcd6d8")
    ds "如果那时候，你还是喜欢我。" id story_route_ds_1ebc55fcd6d8_1
    voice voice_file("v_025797a09c0e")
    ds "就再向我告白一次吧。" id story_route_ds_025797a09c0e_1
    ## 演出: 旁白
    narrator "我轻轻抱住她。" id story_route_ds_9d9a38f60ef8_2
    voice voice_file("v_333e949d441c")
    u "好。" id story_route_ds_333e949d441c_4
    voice voice_file("v_dba1ddb00c5d")
    ds "不许忘记！" id story_route_ds_dba1ddb00c5d_1
    voice voice_file("v_9cf3fe2a0a35")
    u "不会忘。" id story_route_ds_9cf3fe2a0a35_1
    narrator "她终于松开手。" id story_route_ds_140dc63192f0_1
    narrator "笑着向我挥了挥。" id story_route_ds_1400e9b0ff80_1
    voice voice_file("v_f7a68041683d")
    ds "那我走啦！" id story_route_ds_f7a68041683d_1
    ## 演出: 旁白
    narrator "她转身走向安检口。" id story_route_ds_1c1b0705df06_1
    narrator "这一次，我没有追上去。" id story_route_ds_fec55433f737_1
    narrator "只是站在原地，看着她的身影一点点消失在人群中。" id story_route_ds_6207c79e0f03_1
    narrator "直到再也看不见。" id story_route_ds_12871aaea785_1

    ## ── 场景: 场景 DS-10｜四年之后 ──
    ## 演出: 时间：四年后 · 东京
    ## 演出: 旁白
    play music "audio/bgm/bgm_transition.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-10 · 四年里各自成长
    scene art_ending_bg31_director_studio_day with trans_dissolve
    narrator "四年过去了。" id story_route_ds_0252de0368b6_1
    scene art_ending_cg_ds10_growth_work with trans_dissolve
    narrator "大学毕业以后，我一直从事影像创作。" id story_route_ds_6f1e3b70afe7_1
    narrator "最初只是帮人拍摄一些短片和宣传视频。" id story_route_ds_4091ccf2bc70_1
    narrator "后来开始独立执导作品。" id story_route_ds_14758b2eb3e0_1
    narrator "虽然过程并不顺利，但我终于逐渐在这个行业里站稳了脚跟。" id story_route_ds_0f0082eb0237_1
    narrator "曾经一起参加电影研究社的朋友们，也陆续走上了不同的道路。" id story_route_ds_50cce2b04deb_1
    narrator "有人成为摄影师。" id story_route_ds_831692140026_1
    narrator "有人从事后期制作。" id story_route_ds_1673427d90c9_1
    narrator "也有人离开了电影行业。" id story_route_ds_7de147094161_1
    narrator "偶尔，我们还会聚在一起，聊起高中时那场文化祭。" id story_route_ds_021798e8b345_1
    ## 演出: 旁白
    scene art_ending_bg31_director_studio_day with trans_dissolve
    show art_ending_pr27_creative_works as story_prop at story_prop_pos with trans_dissolve
    narrator "DeepSeek 在法国的生活也逐渐步入正轨。" id story_route_ds_b935127d0620_1
    narrator "她最初参加的是写作培训。" id story_route_ds_7fa9ef44779f_1
    narrator "后来开始发表短篇小说。" id story_route_ds_7c756b509bd9_1
    narrator "再后来，她的作品得到了出版社的认可。" id story_route_ds_238d7d7b7381_1
    narrator "我偶尔会在网上看到她的名字。" id story_route_ds_2c67124ba3d9_1
    narrator "她不再是那个总担心自己写得不好的女孩。" id story_route_ds_986604964c09_1
    narrator "而是真正拥有读者的小说家。" id story_route_ds_994c12f2af2b_1
    narrator "我们没有完全失去联系。" id story_route_ds_632f36b0aeb0_1
    hide story_prop with trans_dissolve
    narrator "逢年过节时，偶尔会互相问候。" id story_route_ds_b3bcb1167bca_1
    narrator "有时，她会发来新作品的链接。" id story_route_ds_f15135c552ac_1
    narrator "我也会把自己的电影预告片发给她。" id story_route_ds_140c0c1b9eeb_1
    narrator "但我们都没有再提起机场的约定。" id story_route_ds_67bc32a7a8e5_1
    ## 演出: 旁白
    narrator "这四年里，我也逐渐明白了一件事。" id story_route_ds_078e0689fe8b_1
    narrator "我们并不是因为谁不够努力，才曾经走散。" id story_route_ds_5dbafb07263c_1
    narrator "只是那时候的我们，都还没有能力承担自己想要的未来。" id story_route_ds_97e7120c7ae5_1

    ## ── 场景: 场景 DS-11｜重逢 ──
    ## 演出: 时间：秋天 · 文学作品改编交流会
    ## 演出: 旁白
    play music "audio/bgm/bgm_transition.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-11 · 名单上熟悉的名字
    scene art_ending_bg32_adaptation_forum_day with trans_dissolve
    narrator "那天，我受邀参加一场文学作品改编交流会。" id story_route_ds_ea957fa512f6_1
    narrator "主办方希望寻找一些适合改编成电影的小说。" id story_route_ds_9e181a5cb525_1
    narrator "我提前来到会场。" id story_route_ds_64466b796e64_1
    show art_ending_pr28_forum_book_list as story_prop at story_prop_pos with trans_dissolve
    narrator "工作人员递给我一份作品名单。" id story_route_ds_826b043403d4_1
    narrator "我随手翻开。" id story_route_ds_0a779e91221a_1
    narrator "直到看见其中一个熟悉的名字。" id story_route_ds_b75edef88dab_1
    narrator "DeepSeek。" id story_route_ds_7c0be0110e83_2
    narrator "我愣住了。" id story_route_ds_8e1a451c2128_1
    narrator "名单上写着，她已经成为一位受到关注的青年小说家。" id story_route_ds_f60c8966c185_1
    narrator "这次带来的作品，是一部关于青春、成长和错过的长篇小说。" id story_route_ds_b97398149cd4_1
    narrator "书名叫《候鸟》。" id story_route_ds_8619ae654238_1
    ## 演出: 旁白
    narrator "我慢慢翻开简介。" id story_route_ds_1495a3de08cb_1
    hide story_prop with trans_dissolve
    narrator "故事里的少年曾经成绩很差。" id story_route_ds_1a1b75c239b5_1
    narrator "后来，他遇见了一位愿意帮助自己的女孩。" id story_route_ds_55fb4014b992_1
    narrator "他们一起努力，一起成长。" id story_route_ds_010b67ff9e26_1
    narrator "最终，却因为不同的选择而分别。" id story_route_ds_e486812eb489_1
    narrator "多年以后，两人再次相遇。" id story_route_ds_3e631cce34c9_1
    narrator "我看着那段简介，突然想起高中时的电影研究社。" id story_route_ds_ea0cfe8263ea_1
    narrator "那时候，DeepSeek 也曾经写过一个叫《候鸟》的故事。" id story_route_ds_79eb0835314b_1
    voice voice_file("v_9a214723f7bb")
    mystery "诶？" id story_route_ds_9a214723f7bb_1
    narrator "身后突然传来熟悉的声音。" id story_route_ds_9adefa9c2421_1
    voice voice_file("v_98fe969b1d55")
    mystery "你该不会……" id story_route_ds_98fe969b1d55_1
    narrator "我回过头。" id story_route_ds_7ebb32893b81_1
    narrator "一个蓝发少女站在不远处。" id story_route_ds_11817cd38e41_1
    narrator "她穿着浅色外套，手里抱着几本书。" id story_route_ds_43e94bbe2bcd_1
    narrator "四年过去，她的模样已经比以前成熟了许多。" id story_route_ds_a3760244caf9_1
    narrator "可那双明亮的眼睛，依然和第一次见面时一样。" id story_route_ds_0b3ad3eedfb0_1
    scene art_ending_cg18_forum_reunion with trans_dissolve
    voice voice_file("v_7d1bffc200ac")
    ds "User？！" id story_route_ds_7d1bffc200ac_1
    voice voice_file("v_d7f72fc4008d")
    u "……DeepSeek。" id story_route_ds_d7f72fc4008d_1
    narrator "她愣了几秒。" id story_route_ds_32eb9b617119_1
    scene art_ending_bg32_adaptation_forum_day with trans_dissolve
    show art_ending_ds_mat_spring_blush as ds at sprite_pos_left with trans_dissolve
    narrator "然后突然笑了起来。" id story_route_ds_7641fa43025c_1
    voice voice_file("v_35a43689ef83")
    ds "真的是你呀！" id story_route_ds_35a43689ef83_1
    voice voice_file("v_1427732ec408")
    ds "我还以为自己看错了呢！" id story_route_ds_1427732ec408_1
    ## 演出: 旁白
    narrator "她跑到我面前。" id story_route_ds_a2c751d9745d_1
    narrator "和高中时一样，差点撞上我。" id story_route_ds_1149864566d8_1
    voice voice_file("v_b037fea629e7")
    u "小心！" id story_route_ds_b037fea629e7_1
    voice voice_file("v_a85e48500e01")
    ds "哇！" id story_route_ds_a85e48500e01_1
    narrator "她慌忙停住。" id story_route_ds_98ddedf565df_1
    narrator "然后有些不好意思地挠了挠头。" id story_route_ds_e0ed04cfbbe4_1
    voice voice_file("v_f70b16a8e752")
    ds "嘿嘿……" id story_route_ds_f70b16a8e752_1
    voice voice_file("v_56c737433ada")
    ds "好久不见！" id story_route_ds_56c737433ada_1
    voice voice_file("v_979561950902")
    u "好久不见。" id story_route_ds_979561950902_1

    ## ── 场景: 场景 DS-12｜最后一次告白 ──
    ## 演出: 时间：交流会结束后 · 公园 · 傍晚
    ## 演出: 旁白
    play music "audio/bgm/bgm_deepseek.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-12 · 现在的我们再次喜欢
    scene art_ending_bg33_reunion_park_sunset with trans_dissolve
    narrator "交流会结束后，我们一起去了附近的公园。" id story_route_ds_3e504147e07a_1
    narrator "四年没有真正见面。" id story_route_ds_ff2672dcd230_1
    narrator "可一旦聊起来，却发现彼此仍然有说不完的话。" id story_route_ds_9298f35bf975_1
    narrator "她告诉我在法国的生活。" id story_route_ds_5420c7cd3567_1
    narrator "告诉我第一次投稿失败时有多难过。" id story_route_ds_4a32435a914e_1
    narrator "也告诉我，自己的第一本小说正式出版时，曾经一个人高兴得睡不着觉。" id story_route_ds_cde0204f0ea5_1
    narrator "我则告诉她这些年拍电影的经历。" id story_route_ds_9d9bdac7c6cf_1
    narrator "那些失败的项目。" id story_route_ds_98af45473247_1
    narrator "那些反复修改的剧本。" id story_route_ds_c36a90f55492_1
    narrator "还有第一次在银幕上看到自己名字时的心情。" id story_route_ds_a9fce3d03552_1
    show art_ending_ds_mat_spring_neutral as ds at sprite_pos_left with trans_dissolve
    voice voice_file("v_052da7680b7b")
    ds "哇……" id story_route_ds_052da7680b7b_1
    voice voice_file("v_4472460255fd")
    ds "感觉大家都变得好厉害呀。" id story_route_ds_4472460255fd_1
    voice voice_file("v_b8c1915d6dc1")
    u "你也是。" id story_route_ds_b8c1915d6dc1_1
    voice voice_file("v_a7782c7ec24c")
    ds "嘿嘿。" id story_route_ds_a7782c7ec24c_3
    narrator "她笑了笑。" id story_route_ds_bb3f418c0b76_1
    narrator "然后突然问道。" id story_route_ds_cc5314241f33_1
    voice voice_file("v_f65b503e9361")
    ds "对了。" id story_route_ds_f65b503e9361_1
    voice voice_file("v_b92055a42aa7")
    ds "你现在有女朋友吗？" id story_route_ds_b92055a42aa7_1
    show art_ending_ds_mat_spring_blush as ds at sprite_pos_left with trans_dissolve
    voice voice_file("v_64555b5aeaf3")
    u "没有。" id story_route_ds_64555b5aeaf3_3
    narrator "她愣了一下。" id story_route_ds_05400f1a53de_1
    voice voice_file("v_290e218b9aad")
    ds "……真的？" id story_route_ds_290e218b9aad_2
    voice voice_file("v_9e021948b332")
    u "真的。" id story_route_ds_9e021948b332_2
    voice voice_file("v_7d1779d2a76a")
    ds "哦……" id story_route_ds_7d1779d2a76a_1
    narrator "她低下头。" id story_route_ds_00d82bb20a31_7
    narrator "过了一会儿，又小声说道。" id story_route_ds_9df87a61e1cc_1
    voice voice_file("v_41d9143a35a8")
    ds "我也没有。" id story_route_ds_41d9143a35a8_1
    ## 演出: 旁白
    narrator "我们沉默了一会儿。" id story_route_ds_fc2086d27651_1
    narrator "夕阳落在公园的湖面上。" id story_route_ds_c72ebd6cdeee_1
    narrator "和很多年前，她第一次向我告白的那天很像。" id story_route_ds_950a0dd2ea92_1
    voice voice_file("v_0a84887f827d")
    ds "User。" id story_route_ds_0a84887f827d_2
    voice voice_file("v_7235f2204469")
    u "嗯？" id story_route_ds_7235f2204469_5
    voice voice_file("v_eb17f5f7e133")
    ds "你还记得机场那天，我说过的话吗？" id story_route_ds_eb17f5f7e133_1
    voice voice_file("v_05a3d59649dc")
    u "记得。" id story_route_ds_05a3d59649dc_2
    voice voice_file("v_45ad20b4e245")
    ds "我说，如果以后再见面，你还是喜欢我……" id story_route_ds_45ad20b4e245_1
    narrator "她停住了。" id story_route_ds_3311f2cffd34_1
    narrator "脸颊一点点红起来。" id story_route_ds_1ca5cfbe5530_1
    voice voice_file("v_146160c15a85")
    ds "就再向我告白一次。" id story_route_ds_146160c15a85_1
    ## 演出: 旁白
    narrator "我看着她。" id story_route_ds_e2f5aab3b666_2
    narrator "四年前，她离开时，我们都不知道未来会变成什么样。" id story_route_ds_8321edd0b0f0_1
    narrator "那时候的我们，只能把希望寄托在一个遥远的约定上。" id story_route_ds_52609f9b7aae_1
    narrator "可现在，我们已经走过了各自的道路。" id story_route_ds_5656eb1c65f9_1
    narrator "也终于有能力认真面对自己的选择。" id story_route_ds_677932816fec_1
    narrator "我走到她面前。" id story_route_ds_a7da6107f6fb_3
    voice voice_file("v_c5f965228eed")
    u "DeepSeek。" id story_route_ds_c5f965228eed_3
    voice voice_file("v_0e748d627265")
    ds "嗯？" id story_route_ds_0e748d627265_3
    voice voice_file("v_beb8abdad9de")
    u "我喜欢你。" id story_route_ds_beb8abdad9de_3
    narrator "她睁大眼睛。" id story_route_ds_1ee0b57979fb_1
    voice voice_file("v_22fbb41a64c6")
    u "不是因为我们以前交往过。" id story_route_ds_22fbb41a64c6_1
    voice voice_file("v_a123a03736a5")
    u "也不是因为那个机场的约定。" id story_route_ds_a123a03736a5_1
    voice voice_file("v_33f2977f7e19")
    u "是因为四年后的今天，我再次见到你，依然想和你一起生活。" id story_route_ds_33f2977f7e19_1
    voice voice_file("v_9d09b3503d59")
    u "一起创作，一起旅行。" id story_route_ds_9d09b3503d59_1
    voice voice_file("v_6ca90f7105bf")
    u "也一起度过那些没有什么特别事情发生的日子。" id story_route_ds_6ca90f7105bf_1
    show art_ending_ds_mat_spring_teary_smile as ds at sprite_pos_left with trans_dissolve
    narrator "她的眼泪突然落了下来。" id story_route_ds_bde6d158365f_1
    voice voice_file("v_2803f44edf18")
    ds "……笨蛋。" id story_route_ds_2803f44edf18_2
    voice voice_file("v_7235f2204469")
    u "嗯？" id story_route_ds_7235f2204469_6
    voice voice_file("v_09fae06b8d7b")
    ds "你怎么还是这么会让人哭呀。" id story_route_ds_09fae06b8d7b_1
    narrator "她一边擦眼泪，一边笑。" id story_route_ds_324066be4229_1
    voice voice_file("v_1b1e0bcbd65e")
    ds "不过……" id story_route_ds_1b1e0bcbd65e_2
    narrator "她抬起头。" id story_route_ds_54b76a6e010c_5
    voice voice_file("v_3dce870d8db6")
    ds "我也喜欢你。" id story_route_ds_3dce870d8db6_1

    ## ── 场景: 场景 DS-12｜最后一次告白（续） ──
    voice voice_file("v_3dce870d8db6")
    ds "我也喜欢你。" id story_route_ds_3dce870d8db6_2
    voice voice_file("v_4d7e007b2905")
    ds "一直、一直都喜欢着你。" id story_route_ds_4d7e007b2905_1
    ## 演出: 旁白
    narrator "她的声音有些颤抖。" id story_route_ds_f0ac9403763b_1
    voice voice_file("v_607908fecda8")
    ds "在法国的时候，我其实想过很多次。" id story_route_ds_607908fecda8_1
    voice voice_file("v_85b020b54082")
    ds "如果有一天，我们真的又见面了，你已经有了喜欢的人，该怎么办。" id story_route_ds_85b020b54082_1
    voice voice_file("v_6463bc7d4aaf")
    ds "如果你已经忘记了我们的约定，又该怎么办。" id story_route_ds_6463bc7d4aaf_1
    narrator "她低下头，轻轻擦去眼角的泪水。" id story_route_ds_57cad1ac8947_1
    voice voice_file("v_1e091028fe74")
    ds "所以我拼命写故事。" id story_route_ds_1e091028fe74_1
    voice voice_file("v_ed2d74b462f9")
    ds "因为我想，至少要成为一个真正的作家。" id story_route_ds_ed2d74b462f9_1
    voice voice_file("v_340ec356fd93")
    ds "这样的话，就算最后没有和你在一起，我也能告诉自己，这几年没有白白度过。" id story_route_ds_340ec356fd93_1
    voice voice_file("v_5f55f500d924")
    u "……" id story_route_ds_5f55f500d924_4
    voice voice_file("v_c906d17f33c7")
    ds "可是今天看到你的时候……" id story_route_ds_c906d17f33c7_1
    narrator "她忍不住笑了。" id story_route_ds_0e262a80a3c3_1
    voice voice_file("v_1a9c91b0915c")
    ds "我才发现，原来自己还是和以前一样。" id story_route_ds_1a9c91b0915c_1
    voice voice_file("v_afd52e1076e4")
    ds "只要你站在我面前，我就会特别特别开心。" id story_route_ds_afd52e1076e4_1
    ## 演出: 旁白
    narrator "我轻轻握住她的手。" id story_route_ds_ef0f9fc7f4cf_2
    narrator "这一次，她没有像高中时那样害羞地躲开。" id story_route_ds_3b607c84687f_1
    narrator "而是主动回握住我。" id story_route_ds_690eea4a8f81_1
    voice voice_file("v_c5f965228eed")
    u "DeepSeek。" id story_route_ds_c5f965228eed_4
    voice voice_file("v_0e748d627265")
    ds "嗯？" id story_route_ds_0e748d627265_4
    voice voice_file("v_4611287c0b3e")
    u "以后，我们一起走吧。" id story_route_ds_4611287c0b3e_1
    show art_ending_ds_mat_spring_tender as ds at sprite_pos_left with trans_dissolve
    narrator "她抬起头。" id story_route_ds_54b76a6e010c_6
    voice voice_file("v_11325855b49a")
    ds "……嗯！" id story_route_ds_11325855b49a_1
    voice voice_file("v_e2cebce5eac2")
    ds "不过这次，不许再突然说什么暂时分开了！" id story_route_ds_e2cebce5eac2_1
    voice voice_file("v_8ba68d990031")
    u "不会了。" id story_route_ds_8ba68d990031_2
    voice voice_file("v_d573342ad5eb")
    ds "也不许因为工作太忙，就忘记找我！" id story_route_ds_d573342ad5eb_1
    voice voice_file("v_333e949d441c")
    u "好。" id story_route_ds_333e949d441c_5
    voice voice_file("v_71c78d85c5f7")
    ds "还有！以后我的小说，你必须第一个看！" id story_route_ds_71c78d85c5f7_1
    voice voice_file("v_571b8ae6e8a4")
    u "这个要求是不是有点过分？" id story_route_ds_571b8ae6e8a4_1
    voice voice_file("v_9aaeb94af987")
    ds "哪里过分啦！" id story_route_ds_9aaeb94af987_1
    narrator "她鼓起脸颊。" id story_route_ds_0054baff6a13_1
    narrator "我忍不住笑了。" id story_route_ds_d316041b00d7_2
    voice voice_file("v_eac730196c3a")
    u "好，都答应你。" id story_route_ds_eac730196c3a_1
    voice voice_file("v_a7782c7ec24c")
    ds "嘿嘿。" id story_route_ds_a7782c7ec24c_4
    ## 演出: 旁白
    scene art_ending_cg19_park_short_kiss with trans_dissolve
    narrator "她踮起脚尖，轻轻吻了我。" id story_route_ds_6758ff59e45a_1
    narrator "那是一个很短的吻。" id story_route_ds_509fd67d5dfa_1
    narrator "短到我还没来得及反应，她就已经红着脸退开。" id story_route_ds_3b821bc3b262_1
    voice voice_file("v_8ce926661ed7")
    ds "这、这次可是我主动的哦！" id story_route_ds_8ce926661ed7_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_9
    voice voice_file("v_518b61f52c31")
    ds "所以你要好好珍惜！" id story_route_ds_518b61f52c31_1
    ## 演出: 旁白
    narrator "夕阳落在她的蓝发上。" id story_route_ds_60b091626e26_1
    narrator "我突然想起很多年前的那个下午。" id story_route_ds_afe9965d1862_1
    narrator "那时候，她也是这样站在阳光里。" id story_route_ds_4d90dc1be914_1
    narrator "冒冒失失地闯进我的生活。" id story_route_ds_86493ce17f66_1
    narrator "而我曾经以为，那只是一个普通得不能再普通的偶然。" id story_route_ds_bb115795ef4d_1
    narrator "现在才明白。" id story_route_ds_fb3b8ecbb1af_1
    narrator "原来有些相遇，会在很久以后，才显露出它真正的意义。" id story_route_ds_f595e929a0ac_1

    ## ── 场景: 场景 DS-13｜最初的约定，终于实现 ──
    ## 演出: 时间：半年后 · 电影首映礼
    ## 演出: 旁白
    play music "audio/bgm/bgm_deepseek.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-13A · 共同创作仍会争论
    scene art_ending_bg31_director_studio_day with trans_dissolve
    narrator "半年以后，我的新电影终于完成了。" id story_route_ds_f2eff0d36537_1
    narrator "改编自 DeepSeek 的小说《候鸟》。" id story_route_ds_5552b176059e_1
    narrator "这也是我们第一次真正以导演和原作者的身份合作。" id story_route_ds_fa429b607a01_1
    narrator "从剧本修改到拍摄，再到最后的剪辑，我们经历了无数次争论。" id story_route_ds_3c1a3ed344e2_1
    scene art_ending_cg_ds13a_creating_together with trans_dissolve
    narrator "有时候，她会因为我删掉某段情节而生气。" id story_route_ds_a28c694206e5_1
    narrator "有时候，我也会因为她突然修改结局而头疼。" id story_route_ds_6438658517ba_1
    narrator "可无论争论多少次，第二天，我们还是会坐在一起，继续完成剩下的工作。" id story_route_ds_bfa9305f11c0_1
    narrator "就像高中时一样。" id story_route_ds_65d9677eafab_1
    narrator "只是这一次，我们终于能够凭借自己的能力，把当初的梦想变成现实。" id story_route_ds_dbc2d0d52a32_1
    ## 演出: 场景：首映礼后台
    play music "audio/bgm/bgm_deepseek.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-13B · 这本笔记本终于可以归还
    scene art_ending_bg34_premiere_backstage_evening with trans_dissolve
    show art_ending_ds_mat_premiere_flustered as ds at sprite_pos_left with trans_dissolve
    voice voice_file("v_39aa041d99e4")
    ds "User！User！" id story_route_ds_39aa041d99e4_1
    narrator "她慌慌张张地跑过来。" id story_route_ds_64a9b66d7b19_1
    voice voice_file("v_8517678f9232")
    u "怎么了？" id story_route_ds_8517678f9232_4
    voice voice_file("v_48373f2a1822")
    ds "我的笔记本不见了！" id story_route_ds_48373f2a1822_1
    voice voice_file("v_5f55f500d924")
    u "……" id story_route_ds_5f55f500d924_5
    voice voice_file("v_889b6aff98c3")
    ds "怎么办怎么办！我明明记得放在包里的！" id story_route_ds_889b6aff98c3_1
    narrator "我叹了口气。" id story_route_ds_bd68a300332e_1
    show art_ending_pr01_aged_blue_notebook as story_prop at story_prop_pos with trans_dissolve
    narrator "从自己的背包里拿出一本浅蓝色的笔记本。" id story_route_ds_9f4098b5211c_1
    voice voice_file("v_a438ba4976e2")
    u "你是在找这个吗？" id story_route_ds_a438ba4976e2_1
    narrator "她愣住了。" id story_route_ds_be2b60c9df15_2
    voice voice_file("v_9a8068fd217d")
    ds "诶？！" id story_route_ds_9a8068fd217d_2
    voice voice_file("v_75980dab499f")
    ds "怎么会在你那里！" id story_route_ds_75980dab499f_1
    voice voice_file("v_0d46a24bde3d")
    u "刚才你放在化妆台上，差点忘记带走。" id story_route_ds_0d46a24bde3d_1
    voice voice_file("v_4c725d83151b")
    ds "呜……" id story_route_ds_4c725d83151b_1
    narrator "她不好意思地挠了挠头。" id story_route_ds_ffc7ffa116ad_1
    voice voice_file("v_fe9e63f60acd")
    ds "嘿嘿，还是你最可靠了！" id story_route_ds_fe9e63f60acd_1
    ## 演出: 旁白
    narrator "我看着手中的笔记本。" id story_route_ds_04a28201a07e_1
    narrator "封面已经有些破旧。" id story_route_ds_785cc7f197bf_1
    narrator "里面的纸张也因为反复翻阅而微微泛黄。" id story_route_ds_9963bfcb62df_1
    narrator "可第一页上，那些稚嫩的字迹依然清晰。" id story_route_ds_4dc66656817c_1
    narrator "这是我们第一次见面时，她遗失在天台上的那本笔记本。" id story_route_ds_da1130ca9687_1
    narrator "也是我们最初约定一起拍电影的起点。" id story_route_ds_f7922e5eee18_1
    voice voice_file("v_c5f965228eed")
    u "DeepSeek。" id story_route_ds_c5f965228eed_5
    voice voice_file("v_0e748d627265")
    ds "嗯？" id story_route_ds_0e748d627265_5
    hide story_prop with trans_dissolve
    narrator "我把笔记本递给她。" id story_route_ds_0bb224bc0ab0_1
    voice voice_file("v_f85f7d6388d0")
    u "现在可以还给你了。" id story_route_ds_f85f7d6388d0_1
    narrator "她低头看着笔记本。" id story_route_ds_3bd1278d6433_1
    narrator "然后，慢慢抬起头。" id story_route_ds_f44d56913bc6_1
    voice voice_file("v_769900058a2f")
    ds "……啊。" id story_route_ds_769900058a2f_1
    ## 演出: 旁白
    narrator "她终于想起来了。" id story_route_ds_d1b8ca8edd78_1
    narrator "很多年前，在高中母校的天台上，她曾经把这本笔记本交给我。" id story_route_ds_0bf8c162a87d_1
    narrator "她说，等我们真正拍出一部很厉害的电影，就把它还给她。" id story_route_ds_f49926446045_1
    narrator "如今，我们终于做到了。" id story_route_ds_de4934b8b31f_1
    voice voice_file("v_fc9fc315de57")
    ds "……真的拍出来了呢。" id story_route_ds_fc9fc315de57_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_10
    voice voice_file("v_d118ba31a580")
    ds "那时候，我还以为只是一个很遥远的梦想。" id story_route_ds_d118ba31a580_1
    narrator "她轻轻翻开笔记本。" id story_route_ds_abf43a8f0a0d_1
    narrator "看着里面那些歪歪扭扭的文字。" id story_route_ds_ab7bf453853c_1
    voice voice_file("v_93d7aba45b2d")
    ds "谢谢你。" id story_route_ds_93d7aba45b2d_1
    voice voice_file("v_f2fc25188ca1")
    u "怎么突然这么客气？" id story_route_ds_f2fc25188ca1_1
    voice voice_file("v_3a462aefc239")
    ds "因为……" id story_route_ds_3a462aefc239_1
    narrator "她抬起头，眼睛里泛起泪光。" id story_route_ds_6f70539af9f8_1
    voice voice_file("v_a5e2daf7bbe8")
    ds "如果那天你没有捡到我的笔记本，我可能就不会认识你。" id story_route_ds_a5e2daf7bbe8_1
    voice voice_file("v_b17871c3f6d7")
    ds "如果你没有说想把我的故事拍成电影，我可能也不会坚持写到今天。" id story_route_ds_b17871c3f6d7_1
    voice voice_file("v_646f2cc87a2b")
    ds "所以……" id story_route_ds_646f2cc87a2b_1
    scene art_ending_cg20_premiere_notebook_embrace with trans_dissolve
    narrator "她用力抱住我。" id story_route_ds_85bca168a914_1
    voice voice_file("v_33fdfba33083")
    ds "能遇见你，真的太好了！" id story_route_ds_33fdfba33083_1
    ## 演出: 旁白
    narrator "我轻轻抱住她。" id story_route_ds_9d9a38f60ef8_3
    narrator "远处传来工作人员的声音。" id story_route_ds_4cd7bbee873b_1
    voice voice_file("v_e3d0b1197f27")
    staff "导演！原作者！首映马上开始了！" id story_route_ds_e3d0b1197f27_1
    voice voice_file("v_2736d7284037")
    ds "啊啊啊！要迟到了！" id story_route_ds_2736d7284037_1
    scene art_ending_bg34_premiere_backstage_evening with trans_dissolve
    show art_ending_ds_mat_premiere_neutral as ds at sprite_pos_left with trans_dissolve
    narrator "她慌忙松开手。" id story_route_ds_2267e57a477e_1
    narrator "抓起笔记本就往外跑。" id story_route_ds_480915946081_1
    voice voice_file("v_bea7919dfc85")
    u "慢一点！" id story_route_ds_bea7919dfc85_1
    voice voice_file("v_f415dde8eb1a")
    ds "知道啦！" id story_route_ds_f415dde8eb1a_1
    ## 演出: 旁白
    narrator "她跑到门口，又突然转过身。" id story_route_ds_9ffa9ca36085_1
    voice voice_file("v_51a5ecf1d639")
    ds "User！" id story_route_ds_51a5ecf1d639_4
    voice voice_file("v_9ec3c44677b2")
    u "又怎么了？" id story_route_ds_9ec3c44677b2_1
    narrator "她露出一个灿烂的笑容。" id story_route_ds_961f95f9420d_1
    voice voice_file("v_3fb46392dc82")
    ds "下一部电影，也要一起拍哦！" id story_route_ds_3fb46392dc82_1
    voice voice_file("v_3bc23ad5109b")
    u "当然。" id story_route_ds_3bc23ad5109b_1

    ## ── 场景: 场景 DS-14｜尾声：天台上的少女 ──
    ## 演出: 时间：数年后 · 春天 · 高中母校
    ## 演出: 旁白
    play music "audio/bgm/bgm_deepseek.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-14A · 在日常里给彼此留位置
    scene art_ending_bg31_director_studio_evening with trans_dissolve
    narrator "电影上映以后，我们的生活并没有发生什么惊天动地的变化。" id story_route_ds_15e940bd55f1_1
    narrator "DeepSeek 继续写小说。" id story_route_ds_01e5e03829ee_1
    scene art_ending_cg_ds14a_daily_care with trans_dissolve
    narrator "我继续拍电影。" id story_route_ds_e0218afd2a96_1
    narrator "有时候工作很忙，我们也会因为一些琐碎的事情争吵。" id story_route_ds_419a89e4edd8_1
    narrator "她依然会忘记带钥匙，偶尔把手机放进冰箱里，还会在半夜突然把我叫醒，说自己想到了一个绝妙的故事。" id story_route_ds_860f9ed751cb_1
    narrator "我也依然会因为剪辑工作忘记吃饭，或者在拍摄期间连续几天睡眠不足。" id story_route_ds_bc11ec7cfe55_1
    narrator "可我们已经学会了，在忙碌的生活里为彼此留下位置。" id story_route_ds_199b38aed296_1
    narrator "不再要求对方放弃自己的梦想。" id story_route_ds_46b6c32c6096_1
    narrator "也不再因为害怕失去，就逃避应该说出口的话。" id story_route_ds_378abaeba6e3_1
    ## 演出: 场景：高中母校 · 天台
    play music "audio/bgm/bgm_deepseek.mp3" fadeout 1.0 fadein 1.0 if_changed
    ## 美术分景 DS-14B · 天台上的少女与明天
    scene art_ending_bg01_refurbished_spring_day with trans_dissolve
    narrator "那年春天，我们再次回到了最初相遇的地方。" id story_route_ds_37243214047f_1
    narrator "教学楼还是原来的样子。" id story_route_ds_e6f0ed5931c6_1
    narrator "天台的栏杆重新刷过漆。" id story_route_ds_0fa60487e935_1
    narrator "远处的樱花正开得很好。" id story_route_ds_d691440ccde7_1
    narrator "DeepSeek 站在我身边，仰头看着天空。" id story_route_ds_e087e3e3a478_1
    show art_ending_ds_mat_spring_neutral as ds at sprite_pos_left with trans_dissolve
    voice voice_file("v_0a84887f827d")
    ds "User。" id story_route_ds_0a84887f827d_3
    voice voice_file("v_7235f2204469")
    u "嗯？" id story_route_ds_7235f2204469_7
    voice voice_file("v_97fc87e43d5d")
    ds "你还记得我们第一次见面的时候吗？" id story_route_ds_97fc87e43d5d_1
    voice voice_file("v_3bc23ad5109b")
    u "当然。" id story_route_ds_3bc23ad5109b_2
    show art_ending_ds_mat_spring_pout as ds at sprite_pos_left with trans_dissolve
    voice voice_file("v_7d2f22014eaf")
    ds "那时候你是不是觉得我特别笨？" id story_route_ds_7d2f22014eaf_1
    voice voice_file("v_88c9b8aa98f4")
    u "嗯。" id story_route_ds_88c9b8aa98f4_11
    voice voice_file("v_05cb0c12992e")
    ds "诶？！你居然承认了！" id story_route_ds_05cb0c12992e_1
    voice voice_file("v_21023f5d52d3")
    u "毕竟正常人不会从矮墙上掉下来。" id story_route_ds_21023f5d52d3_1
    voice voice_file("v_07d1d982c876")
    ds "那是意外啦！" id story_route_ds_07d1d982c876_1
    narrator "她鼓起脸颊。" id story_route_ds_0054baff6a13_2
    narrator "过了一会儿，又自己笑了起来。" id story_route_ds_343416ed73ee_1
    voice voice_file("v_1b1e0bcbd65e")
    ds "不过……" id story_route_ds_1b1e0bcbd65e_3
    voice voice_file("v_62a8936bb1a2")
    ds "如果再来一次，我还是想在这里遇见你。" id story_route_ds_62a8936bb1a2_1
    voice voice_file("v_5fe64f8c35c7")
    u "为什么？" id story_route_ds_5fe64f8c35c7_2
    voice voice_file("v_33d8145d0d08")
    ds "因为这样，我们就又可以从头开始啦。" id story_route_ds_33d8145d0d08_1
    show art_ending_ds_mat_spring_tender as ds at sprite_pos_left with trans_dissolve
    narrator "她伸出手，轻轻握住我的手。" id story_route_ds_70d0f04583c3_1
    voice voice_file("v_20a1f65bea14")
    ds "一起写故事。" id story_route_ds_20a1f65bea14_1
    voice voice_file("v_b1069936dfd8")
    ds "一起拍电影。" id story_route_ds_b1069936dfd8_1
    voice voice_file("v_04b6a7e07573")
    ds "一起经历好多好多事情。" id story_route_ds_04b6a7e07573_1
    narrator "她转过头。" id story_route_ds_8f02e27534e7_1
    narrator "春天的阳光落在她的脸上。" id story_route_ds_76f243dd4e97_1
    voice voice_file("v_43a109f7b324")
    ds "然后，再一次喜欢上你。" id story_route_ds_43a109f7b324_1
    ## 演出: 旁白
    narrator "我看着她。" id story_route_ds_e2f5aab3b666_3
    narrator "忽然想起那个遥远的下午。" id story_route_ds_7b3134366d96_1
    narrator "一个蓝发少女从天台的矮墙上跌落。" id story_route_ds_302cbd6830b0_1
    narrator "一本浅蓝色的笔记本被遗忘在地上。" id story_route_ds_f4534e2822e3_1
    narrator "一个原本毫无关联的人，就这样走进了我的生活。" id story_route_ds_ceb130056576_1
    narrator "后来，我们经历了告白、误会、分别与重逢。" id story_route_ds_e1b6c58a0cbe_1
    narrator "也曾经因为不够成熟，而差一点失去彼此。" id story_route_ds_0d9079659ff9_1
    narrator "可是现在。" id story_route_ds_b14621245d4f_1
    narrator "她就在我身边。" id story_route_ds_16c22835acc3_1
    voice voice_file("v_c5f965228eed")
    u "DeepSeek。" id story_route_ds_c5f965228eed_6
    voice voice_file("v_0e748d627265")
    ds "嗯？" id story_route_ds_0e748d627265_6
    voice voice_file("v_92dc54d298e8")
    u "以后也请多指教。" id story_route_ds_92dc54d298e8_1
    narrator "她愣了一下。" id story_route_ds_05400f1a53de_2
    scene art_ending_cg21_rooftop_tomorrow with trans_dissolve
    narrator "然后露出熟悉的笑容。" id story_route_ds_e3b7b599ba3d_1
    voice voice_file("v_57cd12ae7731")
    ds "嗯！" id story_route_ds_57cd12ae7731_5
    voice voice_file("v_e17b6eaf7e09")
    ds "以后也要一直一直在一起哦！" id story_route_ds_e17b6eaf7e09_1
    ## 演出: 旁白
    narrator "风吹过天台。" id story_route_ds_bd36251a1c11_1
    narrator "樱花花瓣缓缓落下。" id story_route_ds_eb60a7468fcb_1
    narrator "她牵着我的手，向教学楼的出口走去。" id story_route_ds_71490f44e3b8_1
    narrator "这一次，我们没有再约定遥远的重逢。" id story_route_ds_ad7e10d82d4a_1
    narrator "因为明天早晨醒来，我们仍然能够见到彼此。" id story_route_ds_ca50e9186f8b_1
    ## 演出: BGM：主题曲钢琴版渐起
    ## 演出: 画面渐暗
    ## 演出: 最终独白
    narrator "曾经，我以为爱情是某个必须得到的答案。" id story_route_ds_5e0fcf08bebf_1
    narrator "后来才明白，它更像是两个人共同写下的故事。" id story_route_ds_8ebeba65c084_1
    narrator "会有错误。" id story_route_ds_2ec6ea3340a3_1
    narrator "会有遗憾。" id story_route_ds_9613a1c22ba1_1
    narrator "也会有不得不暂时分别的章节。" id story_route_ds_baac7bebbe39_1
    narrator "但只要彼此仍然愿意继续写下去，故事就不会因为一次分别而结束。" id story_route_ds_a7d1ba2efb80_1
    narrator "那个春天，我在天台上捡到了一本笔记本。" id story_route_ds_7ac92d1cd90f_1
    narrator "而很多年以后，我终于读懂了它最后一页的意义。" id story_route_ds_1902c9e60413_1
    narrator "不是所有相遇都注定会有结局。" id story_route_ds_52e8c54439b4_1
    narrator "但有些人，值得我们在分别之后，再一次坚定地选择。" id story_route_ds_e2648df15ba2_1

    jump ending
