testsuite bgm:
    before testcase:
        $ _test.transition_timeout = 0.01
        $ _test.timeout = 120.0
        run Language(None)
        if not screen "main_menu":
            run MainMenu(confirm=False)
    teardown:
        exit
    testcase scene_music:
        pause 1.5
        assert eval (renpy.music.get_playing() == "audio/bgm/titile_theme.mp3")
        run Start("ch00")
        pause 1.5
        assert eval (renpy.music.get_playing() == "audio/bgm/bgm_deepseek.mp3")
        run MainMenu(confirm=False)
        run Language("japanese")
        run Start("ch01")
        pause 1.5
        assert eval (renpy.music.get_playing() == "audio/bgm/bgm_claude.mp3")
        run MainMenu(confirm=False)
        run Start("ch02")
        advance until "最近、学校ではどうなの？"
        pause 1.5
        assert eval (renpy.music.get_playing() == "audio/bgm/bgm_farewell.mp3")
