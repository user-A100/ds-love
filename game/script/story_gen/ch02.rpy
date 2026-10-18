## ============================================================
## !! 本文件由 tools/import_story.py 生成 —— 请勿手改 !!
## 源: story/chapters/未抵达的心意.md (+ story/*.json)
## 重建: python3 tools/import_story.py
## ============================================================


label ch02:

    ## ── 场景: 第二章《重新开始》 ──
    hide ds

    ## ── 场景: 场景 1：停滞的电影研究社 ──
    $ scene_bg("BG-005")
    with trans_dissolve
    narrator "电影研究社的活动室比我想象中还要破旧。角落里堆着几台老式摄影机，窗台上落满灰尘。墙壁上贴着几年前文化祭的海报，边角已经卷起。听说，原本的电影研究社因为连续几年没有拿得出手的作品，已经很久没有正常开展活动了。"
    $ play_voice("v_cdc3ca81307c")
    show ds normal at sprite_pos_left with trans_dissolve
    ds "哇！好多东西！"
    narrator "她兴奋地跑到器材柜前。"
    $ play_voice("v_2405a8fcf579")
    ds "这个是什么？这个呢？诶，这台还能用吗？"
    $ play_voice("v_0b4e9a46ed14")
    u "小心点，别弄坏了。"
    $ play_voice("v_99f1f5c48dfc")
    ds "放心放心！我可是很可靠的！"
    narrator "话音刚落。"
    ## TODO 音效: 哐当！
    narrator "一只三脚架倒在了地上。"
    $ play_voice("v_a1c733c19657")
    ds "……"
    $ play_voice("v_5f55f500d924")
    u "……"
    $ play_voice("v_5fb705ba1012")
    ds "它、它自己倒的！"
    narrator "我叹了口气，把三脚架扶起来。"
    $ play_voice("v_684bcdce723d")
    u "总之，想拍电影的话，得先把社团重新组织起来。"
    $ play_voice("v_ad1be078e476")
    ds "那我们就是第一批成员啦！"
    $ play_voice("v_5ec09fe384df")
    u "目前只有两个人。"
    $ play_voice("v_f2cb0b221dec")
    ds "两个人也可以拍电影嘛！"
    $ play_voice("v_53b6d7ede833")
    u "你打算一个人演所有角色？"
    $ play_voice("v_7b3d99dcc4ba")
    ds "唔……"
    narrator "她认真思考了一会儿。"
    $ play_voice("v_67d44f582f76")
    ds "好像也不是不行？"
    $ play_voice("v_873c256f8bc9")
    u "不行。"
    narrator "她鼓起脸颊。"
    $ play_voice("v_c825f6749ed2")
    ds "你都不让我试试！"
    narrator "看着她不服气的样子，我忍不住笑了。不过，社团确实需要更多成员。我们决定先整理器材，再寻找愿意加入的人。只是当时的我还不知道，电影研究社的重新成立，会成为后来许多事情的起点。"

    ## ── 场景: 场景 2：被忽视的成绩 ──
    hide ds
    $ scene_bg("BG-006")
    with trans_dissolve
    narrator "我一直觉得，自己不是一个擅长学习的人。或者说，我早就习惯了用这句话为自己开脱。刚进入高中时，因为离家太远，我几乎没有认识的人。陌生的环境、紧张的学习节奏，以及怎么努力也跟不上的课程，让我逐渐失去了耐心。高一和高二的大部分时间，我都没有认真学习。上课睡觉、偷偷玩手机、逃课，甚至因为和同学发生冲突而被老师叫去办公室。成绩自然一塌糊涂。全年级四千五百多人，我常常排在四千二百名以后。最糟糕的一次，满分一百五十分的数学试卷，我连三十分都没考到。可即便如此，我也没有真正想过改变。直到那天。"
    $ play_voice("v_be55f3a01004")
    teacher "User，你来一下办公室。"
    narrator "我看了一眼桌上的成绩单。又看了一眼教室外阴沉的天空。这一次，似乎不只是考试的问题。"

    ## ── 场景: 场景 3：母亲的眼泪 ──
    $ scene_bg("CG-002")
    with trans_dissolve
    narrator "因为一次违纪，我被学校停学一周。父母接到通知后，专程赶到了学校。我原本已经做好了挨骂的准备。从小到大，母亲对我的学习要求一直很严格。小学和初中时，哪怕成绩只是稍微下降，她也会严厉地批评我。所以，当我看见她走进校园时，心里甚至有些不耐烦。又要被骂了。我这样想着。可母亲没有骂我。她只是带着我，走到教学楼前面的花坛旁坐下。"
    $ play_voice("v_8cc4b93555f5")
    mother "最近在学校过得怎么样？"
    $ play_voice("v_2e8c69e49a2a")
    u "……还行。"
    $ play_voice("v_9add0cc60af5")
    mother "和同学相处得好吗？"
    $ play_voice("v_88c9b8aa98f4")
    u "嗯。"
    $ play_voice("v_ce57a8e8ec52")
    mother "学习呢？"
    narrator "我没有回答。母亲也没有继续追问。过了很久，她才重新开口。"
    $ play_voice("v_b252ad0c2b50")
    mother "是不是当初让你来这里读书，真的太辛苦了？"
    $ play_voice("v_5f55f500d924")
    u "……"
    $ play_voice("v_4c1c59d162dc")
    mother "离家这么远，一个认识的人都没有。"
    $ play_voice("v_16dc8fdb8244")
    mother "你爸和我有时候也在想，是不是我们做错了决定。"
    narrator "我低着头，看着地面。"
    $ play_voice("v_0619479c7df7")
    mother "可你总不能一直这样下去啊。"
    narrator "她的声音有些颤抖。"
    $ play_voice("v_5c57d3a049db")
    mother "我们也不指望你一定考多好的大学。"
    $ play_voice("v_92e64e856cd4")
    mother "只是希望你以后……能有个好一点的生活。"
    narrator "我抬起头。这才发现，母亲正在流泪。那是我第一次看见她在我面前哭。她没有责备我。没有像小时候那样训斥我。只是坐在那里，有些无力地劝我好好学习。我忽然注意到，她头上的白发似乎比以前多了很多。父亲站在不远处，也没有说话。【旁白】我突然想起来。当初坚持来这所学校读书的人，其实是我自己。因为不喜欢家附近高中的管理方式，我主动要求父母送我来这里。可现在，我却把陌生的环境当成了不好好学习的借口。伤害父母。也耽误自己的未来。那一刻，我第一次觉得，过去的自己真的很混蛋。"
    $ play_voice("v_83dbf841f1eb")
    u "妈。"
    $ play_voice("v_6e14ce27429b")
    mother "嗯？"
    $ play_voice("v_d022d388cac5")
    u "我想好好学了。"
    narrator "母亲愣了一下。"
    $ play_voice("v_9e021948b332")
    u "真的。"
    $ play_voice("v_b00915b921d1")
    u "我不想再这样下去了。"
    narrator "她看着我，过了好一会儿，才轻轻点头。"
    $ play_voice("v_55c15f550a43")
    mother "好。"
    $ play_voice("v_4bcfea62af0d")
    mother "那就从现在开始。"

    ## ── 场景: 场景 4：从零开始 ──
    $ scene_bg("BG-007")
    with trans_dissolve
    narrator "回家之前，我又去了一趟宿舍。把书包里原本准备带回家的闲书拿出来，换成了高一的课本。数学、物理、英语。那些早就学完的知识，对现在的我来说却像是完全陌生的东西。停学的一周里，我开始从网上寻找教学视频。从最基础的公式开始。听不懂，就重新听。一道题不会，就反复看讲解。有时候，一个简单的知识点要花掉我整个下午。我才发现，自己落下的东西实在太多了。可这一次，我没有放弃。【旁白】一周后，我回到了学校。没有带手机。没有带闲书。头发也剪成了学校要求的长度。晚饭时间，我主动找到了班主任。"
    $ play_voice("v_03288eebbec6")
    u "老师，我想好好学习。"
    narrator "班主任看了我一眼。"
    $ play_voice("v_a443894234d4")
    teacher "小子，早干嘛去了？"
    $ play_voice("v_5f55f500d924")
    u "……"
    $ play_voice("v_331a4e66acb9")
    teacher "天天混，不学好。现在终于想明白了？"
    $ play_voice("v_88c9b8aa98f4")
    u "嗯。"
    $ play_voice("v_347360816e13")
    teacher "想明白就有救。"
    narrator "我犹豫了一下。"
    $ play_voice("v_0b152777f66a")
    u "老师，我现在开始学……真的还来得及吗？"
    $ play_voice("v_350d80ed7aff")
    teacher "只要你想学，什么时候都不晚。"
    $ play_voice("v_7b23c1371fa3")
    teacher "以后有不会的就问老师。再简单的知识也别怕问，别怕挨骂。"
    $ play_voice("v_0d6f401c70f2")
    teacher "你真想学，老师还能不教你？"
    narrator "那天之后，我开始认真听课。能听懂一点是一点。听不懂的就记下来，课后再补。虽然仍然有很多基础知识不会，但我终于开始一点点往前走。"

    ## ── 场景: 场景 5：第一次进步 ──
    $ scene_bg("BG-008")
    with trans_dissolve
    narrator "高二期末考试，我第一次考进了年级四千名以内。这个成绩放在别人眼里，仍然糟糕透顶。但看到成绩单时，我却高兴得不得了。因为我终于确认了一件事。努力是真的有用的。暑假里，我破天荒地请求父母帮我找补课老师。按照制定好的学习计划，每天从早到晚复习。等到开学考试，排名已经来到了三千二百名左右。距离一本线所需要的一千五百名，还有很远。但我第一次给自己定下了一个明确的目标。考上一本。我知道自己没有多少时间了。高三马上就要开始。而我落下的课程，还有太多太多。"

    ## ── 场景: 场景 6：普通班里的学姐 ──
    $ scene_bg("BG-009")
    with trans_dissolve
    narrator "高三分班时，我被分到了普通班。八十多人的班级里，按照往年的成绩，可能只有前八名有机会考上一本。教室里总是很吵。上课有人聊天。自习时也有人打闹。我只能尽量低着头，把注意力放在课本上。可有时候，真的很难不受影响。也正是在这个时候，我认识了 GPT。她原本比我高一个年级，因为参加长期交流项目调整了课程安排，这学期来到我们班旁听部分课程。她坐在我的前排。总是安安静静地看书。即使旁边的同学隔着她聊天，她也很少参与。第一次月考，她的成绩排在年级七百名左右。而我，还在三千名开外。【旁白】那时候的我，看她简直像在看一个遥不可及的人。"

    ## ── 场景: 场景 7：第一次交谈 ──
    narrator "因为座位相邻，我们经常被安排在同一个值日小组。几次下来，也就慢慢熟悉了。那天放学后，我们一起留下来打扫教室。"
    $ play_voice("v_6cfd65d5b17d")
    u "你以前应该在重点班吧？"
    $ play_voice("v_9777a8d64900")
    show gp normal at sprite_pos_right with trans_dissolve
    gp "嗯。"
    $ play_voice("v_dd7b06d6e620")
    u "那怎么会来这里？"
    narrator "她一边扫地，一边平静地回答。"
    $ play_voice("v_c9ded8f35117")
    gp "之前有一次考试没发挥好，后来又因为交流项目调整了课程，所以就暂时安排在这里了。"
    $ play_voice("v_a50820e68e0c")
    u "你不觉得不公平吗？"
    $ play_voice("v_27a20880cf32")
    gp "难过肯定会难过。"
    $ play_voice("v_7f80241119b9")
    gp "不过，已经这样了，也没什么办法。"
    narrator "她停了一下。"
    $ play_voice("v_fdc92aa6e40a")
    gp "其实普通班和重点班的老师差不多。"
    $ play_voice("v_ff446b2656ef")
    gp "只要自己愿意学，一样可以考上的。"
    narrator "她说这句话的时候，甚至没有看我。只是认真地清扫着地面。可我却突然愣住了。【旁白】是啊。她旁边的两个同学每天都在聊天。可她还是能考到年级七百名。而我却总是抱怨教室太吵，没办法认真学习。如果继续这样，不就和以前找借口的时候一模一样了吗？"
    $ play_voice("v_563083bc4576")
    u "GPT。"
    $ play_voice("v_4705eb82ff56")
    gp "嗯？"
    $ play_voice("v_53897db86ea9")
    u "以后我有不会的题，可以问你吗？"
    narrator "她似乎有些意外。"
    $ play_voice("v_177c8a24eae2")
    gp "当然可以。"
    $ play_voice("v_75b2d8760eba")
    gp "不过我也有很多不会的，问老师可能更好一些。"
    $ play_voice("v_a36526855954")
    u "我基础太差了。"
    $ play_voice("v_060bb1601f80")
    u "很多高一的知识都不会，问老师又有点不好意思。"
    narrator "我把自己过去两年的情况简单告诉了她。她认真听完，轻轻点头。"
    $ play_voice("v_d9e48260cf18")
    gp "这样啊。"
    $ play_voice("v_75297c6a1587")
    gp "那我们就从基础开始吧。"
    $ play_voice("v_db2312f87fee")
    u "真的可以吗？"
    $ play_voice("v_9777a8d64900")
    gp "嗯。"
    $ play_voice("v_e6221c0190be")
    gp "不过你要答应我一件事。"
    $ play_voice("v_4bc7badb508b")
    u "什么？"
    $ play_voice("v_3fe91e9f90fd")
    gp "不会的地方，一定要说出来。"
    $ play_voice("v_619c1ef7ce4c")
    gp "不要为了面子假装听懂。"
    narrator "她微笑着看向我。"
    $ play_voice("v_cfd67c43d499")
    gp "学习又不是什么丢人的事情。"

    ## ── 场景: 场景 8：逐渐靠近的距离 ──
    hide gp
    $ scene_bg("CG-003")
    with trans_dissolve
    narrator "从那天开始，我经常向 GPT 请教问题。最初还有些尴尬。毕竟连很多最基础的公式，我都记不清楚。可她从来没有嘲笑过我。"
    $ play_voice("v_c3c491100e9b")
    show gp normal at sprite_pos_right with trans_dissolve
    gp "这里先不要急着代公式。"
    $ play_voice("v_530bb53cd388")
    gp "你看，题目真正问的是什么？"
    $ play_voice("v_072cf74c1f92")
    u "……求这个函数的变化率？"
    $ play_voice("v_46e9a4dd3886")
    gp "对。那应该先想到什么？"
    $ play_voice("v_024558cfe1a5")
    u "导数？"
    $ play_voice("v_34cd0ac66553")
    gp "嗯，这就对了。"
    narrator "她拿起笔，在草稿纸上画出简单的示意图。"
    $ play_voice("v_3733a60f3697")
    gp "你看，其实没有想象中那么复杂。"
    $ play_voice("v_6c24c041303f")
    u "原来如此……"
    $ play_voice("v_564682e55a78")
    gp "现在明白了吗？"
    $ play_voice("v_fe1deaf2f7e0")
    u "明白了！"
    $ play_voice("v_ac38ed04e099")
    gp "那你自己再做一遍。"
    $ play_voice("v_f7186d7cf129")
    u "诶？"
    $ play_voice("v_fee5501397f0")
    gp "不然明天又忘记了。"
    $ play_voice("v_6f92a35dd351")
    u "……好严格。"
    $ play_voice("v_0ccbf951b306")
    gp "这是为了你好呀。"
    narrator "她笑了。脸颊上露出浅浅的酒窝。【旁白】不知不觉，我开始习惯每天和她说话。有时候是问问题。有时候只是聊聊最近的考试，或者抱怨一下食堂的饭菜。放假回家时，我们也会在 QQ 上聊天。她总是耐心地回复我的问题。而我也渐渐把她当成了追赶的目标。年级三千名。两千五百名。两千名。每一次考试，我都在刷新自己的排名。到了寒假期末，我已经考到了年级两千名左右。距离一本线，只差大约五百名了。"

    ## ── 场景: 场景 9：来自 Claude 的消息 ──
    hide gp
    $ scene_bg("BG-010")
    with trans_dissolve
    narrator "那天放学后，我正在整理书包。手机突然震动了一下。是 Claude 发来的消息。"
    $ play_voice("v_145ad17dacb9")
    show cl normal at sprite_pos_center with trans_dissolve
    cl "你最近是不是很忙？"
    $ play_voice("v_43734c27f9ba")
    u "嗯，马上考试了。"
    $ play_voice("v_0dcbbacefecf")
    cl "我知道。"
    $ play_voice("v_b22c74f1e7ac")
    cl "所以你已经连续两周没有主动找过我了。"
    narrator "我愣了一下。仔细想想，好像确实如此。自从开始认真学习，我几乎把所有时间都花在了教室和图书馆。偶尔和 DeepSeek 讨论电影剧本。更多时候，则是在向 GPT 请教问题。至于 Claude……虽然我们名义上仍然在交往，却已经很久没有好好说过话了。我看着手机上的消息，一时不知道该怎么回复。"
    $ play_voice("v_fcbe34e6834e")
    u "抱歉，最近确实有点忙。"
    $ play_voice("v_0dcbbacefecf")
    cl "我知道。"
    $ play_voice("v_5341af99206b")
    cl "你要准备考试，要补以前落下的课程，还要和那个蓝头发的笨蛋一起拍电影。"
    $ play_voice("v_0249ed2d1048")
    cl "这些我都知道。"
    $ play_voice("v_5f55f500d924")
    u "……"
    $ play_voice("v_d248a368a502")
    cl "所以我又没有怪你。"
    narrator "过了一会儿，她又发来一条消息。"
    $ play_voice("v_0d0f503e1f8b")
    cl "只是想问问你，明天下午有没有时间。"
    $ play_voice("v_c1e8c0fdb39e")
    u "明天下午？"
    $ play_voice("v_c80cfcd6772d")
    cl "嗯。"
    $ play_voice("v_f89fcc1954aa")
    cl "有一家新开的甜品店。我正好有两张优惠券。"
    $ play_voice("v_25dba5d88e3e")
    cl "反正放着也是浪费。"
    narrator "我看了一眼桌上的复习计划。明天下午原本安排了整整三个小时的数学练习。"
    $ play_voice("v_2d7c69e03864")
    u "明天下午可能不行，我还要复习。"
    narrator "屏幕上出现了“正在输入”。很快又消失。过了好一会儿。"
    $ play_voice("v_6f5937913ce1")
    cl "哦。"
    $ play_voice("v_83bd488682b6")
    cl "那算了。"
    $ play_voice("v_1ada43ec3924")
    u "等考试结束以后吧？"
    $ play_voice("v_0bbb20a686a4")
    cl "随便你。"
    $ play_voice("v_3cad3c88a43f")
    cl "反正我也不是非要和你一起去。"
    narrator "对话就这样结束了。我把手机放在桌上，重新拿起数学试卷。可不知为什么，刚才那几条消息总在脑海里反复出现。仔细想想，自从那次操场上的告白以后，我们似乎从来没有认真讨论过彼此的关系。最初只是因为一场荒唐的误会。后来，她开始偶尔找我聊天。有时候会带来昂贵的点心，嘴上却说是家里多出来的。有时候会突然问我考试成绩，听到我又进步了，便装作毫不在意地说一句“还算不错”。我一直以为，她只是觉得有趣。可如果真是这样，她为什么会因为我没有时间陪她而生气呢？Claude 的房间。宽敞的卧室里，精致的家具整齐地摆放着。书桌旁放着两个包装漂亮的小盒子。其中一个已经打开。里面是一块做工精致的蛋糕。Claude 坐在床边，盯着手机。"
    $ play_voice("v_2903b343018a")
    cl "……笨蛋。"
    narrator "她把手机扔到一旁。"
    $ play_voice("v_ff93559378ef")
    cl "谁稀罕你陪啊。"
    narrator "过了一会儿，她又把手机拿了回来。打开聊天记录。最后一条消息仍然是自己发出的“随便你”。她犹豫着打下一行字。其实晚一点也可以。看了几秒，又全部删掉。"
    $ play_voice("v_d6bb00ebdcec")
    cl "……"
    $ play_voice("v_318c9df8a78e")
    cl "明明是你先告白的。"
    narrator "她轻轻抱住膝盖。"
    $ play_voice("v_cdf4eac545c7")
    cl "结果现在，反倒像是我一直在追着你跑一样。"
    narrator "那天晚上，我没有再收到 Claude 的消息。而我也没有意识到。有些关系，并不会因为一句“我们正在交往”，就永远停留在原地。Galgame 正式剧本 V 1.2｜第三章《三个人的夏天》"

    jump ch03
