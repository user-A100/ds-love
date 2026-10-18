## Ren'Py 8.5.3 engine smoke tests. Run: renpy.py <project> test japanese
testsuite japanese:
    before testcase:
        $ _test.transition_timeout = 0.01
        $ _test.timeout = 10.0
        run Language("japanese")
        if not screen "main_menu":
            run MainMenu(confirm=False)

    teardown:
        exit

    testcase opening_and_language_switch:
        run Start("ch00")
        assert "その日、俺はただ静かな場所を探していただけだった。" timeout 2.0
        run Language(None)
        assert "那天，我原本只是想找个安静的地方。" timeout 2.0
        run Language("japanese")
        assert "その日、俺はただ静かな場所を探していただけだった。" timeout 2.0
        advance
        assert "校舎の屋上には" timeout 2.0

    testcase chapter_navigation:
        run ShowMenu("chapter_select")
        assert "第四章 · 届かない恋" timeout 2.0
        assert "DeepSeekルート · 最初の約束" timeout 2.0
        click "第四章 · 届かない恋"
        assert screen "say"
        assert eval (_preferences.language == "japanese")

    testcase missing_voice_is_silent:
        assert eval (voice_file("missing-test-audio") == "<silence 0.01>")

    testcase deepseek_route:
        $ _test.timeout = 120.0
        run Start("ch06")
        advance until screen "choice"
        assert "DeepSeekに会いに行く"
        assert "Claudeに会いに行く"
        assert "GPTに会いに行く"
        assert "誰にも連絡しない"
        click "DeepSeekに会いに行く"
        advance until "プレイしていただき、ありがとうございました。"

    testcase unfinished_routes:
        run Start("route_normal")
        assert "本文はまだ収録されていません" timeout 2.0
        advance until screen "main_menu"

    testcase ending:
        run Start("ending")
        assert "本編は、ここまでです。" timeout 2.0
        advance
        assert "プレイしていただき、ありがとうございました。" timeout 2.0
