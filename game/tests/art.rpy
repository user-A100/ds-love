## Native engine checks; no game packaging or publishing.
testsuite art:
    before testcase:
        $ _test.transition_timeout = 0.01
        $ _test.timeout = 120.0
        $ _test.screenshot_directory = ".cache/art-screenshots"
        run Language(None)
        if not screen "main_menu":
            run MainMenu(confirm=False)

    teardown:
        exit

    testcase opening_cg_and_recovery:
        run Start("ch00")
        assert eval renpy.showing("art_act01_bg_rooftop_spring_day")
        assert eval not renpy.showing("ds")
        advance until "我还没来得及反应，就被撞得坐在地上。"
        assert eval renpy.showing("art_act01_cg01_rooftop_collision")
        assert eval not renpy.showing("ds")
        screenshot "opening-cg.png"
        advance until "你没事吧？！"
        assert eval renpy.showing("ds")
        assert eval not renpy.showing("art_act01_cg01_rooftop_collision")
        screenshot "opening-sprite.png"

    testcase japanese_opening_sprite:
        run Language("japanese")
        run Start("ch00")
        advance until "だ、大丈夫か！？"
        assert eval renpy.showing("ds")
        screenshot "japanese-opening-sprite.png"

    testcase all_heroines_in_both_languages:
        run Start("ch01")
        advance until "你从刚才开始就在看我吧？"
        pause 1.0
        screenshot "chinese-claude.png"
        run MainMenu(confirm=False)
        run Start("ch02")
        advance until "之前有一次考试没发挥好"
        pause 1.0
        screenshot "chinese-gpt.png"
        run MainMenu(confirm=False)
        run Language("japanese")
        run Start("ch01")
        advance until "あんた、さっきからずっと私を見てるわよね？"
        pause 1.0
        screenshot "japanese-claude.png"
        run MainMenu(confirm=False)
        run Start("ch02")
        advance until "前に一度テストでうまくいかなくて"
        pause 1.0
        screenshot "japanese-gpt.png"

    testcase handover_and_route_choice:
        run Start("ch06")
        advance until "她把厚厚一摞稿纸递给我。"
        assert eval renpy.showing("art_act06_cg_c602_final_manuscript_handover")
        assert eval not renpy.showing("ds")
        screenshot "manuscript-cg.png"
        advance until screen "choice"
        assert eval renpy.showing("art_act06_bg29_crossing_sunset")
        assert "去找 DeepSeek"
        assert "去找 Claude"
        assert "去找 GPT"
        screenshot "route-choice.png"

    testcase common_line_walkthrough:
        $ _test.timeout = 300.0
        run Start("ch01")
        advance until screen "choice"
        assert eval renpy.showing("art_act06_bg29_crossing_sunset")

    testcase performance_cg_timing:
        run Start("ch03")
        advance until "我有点紧张。"
        assert eval not renpy.showing("art_act03_cg04_cultural_festival")
        advance until "最后，DeepSeek 也加入了合唱。"
        assert eval renpy.showing("art_act03_cg04_cultural_festival")
        assert eval not renpy.showing("ds")
        screenshot "performance-timing.png"

    testcase route_night_and_departures:
        run Start("route_ds")
        advance until "我收起手机，向车站跑去。"
        assert eval renpy.showing("art_ds_route_bg30_university_night")
        advance until "我赶到活动室时，DeepSeek 正趴在桌上写东西。"
        assert eval renpy.showing("art_ds_route_bg26_filmclub_night")
        advance until "门关上的瞬间，音乐教室里重新响起钢琴声。"
        assert eval not renpy.showing("cl")
        screenshot "claude-departure.png"
        advance until "我走出咖啡馆。"
        assert eval not renpy.showing("gp")
        screenshot "gpt-departure.png"

    testcase mother_first_dialogue:
        run Start("ch02")
        advance until "最近在学校过得怎么样？"
        assert eval renpy.showing("art_act02_cg_c203_mother")
        screenshot "mother-first-dialogue.png"
        run MainMenu(confirm=False)
        run Language("japanese")
        run Start("ch02")
        advance until "最近、学校ではどうなの？"
        assert eval renpy.showing("art_act02_cg_c203_mother")
        screenshot "japanese-mother-first-dialogue.png"
