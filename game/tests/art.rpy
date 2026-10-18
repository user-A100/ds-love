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
        advance until eval renpy.showing("cl")
        screenshot "chinese-claude.png"
        run MainMenu(confirm=False)
        run Start("ch02")
        advance until eval renpy.showing("gp")
        screenshot "chinese-gpt.png"
        run MainMenu(confirm=False)
        run Language("japanese")
        run Start("ch01")
        advance until eval renpy.showing("cl")
        screenshot "japanese-claude.png"
        run MainMenu(confirm=False)
        run Start("ch02")
        advance until eval renpy.showing("gp")
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
