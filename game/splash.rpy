## splash.rpy

# This is where the disclaimer and the splash screen reside in.

## The disclaimer screen that appears when the game starts.
label splashscreen:

    $ quick_menu = False

    $ show_choose_language = not persistent.has_chosen_language and translations

    scene black

    ## Switch to language selector. Borrowed from Ren'Py
    if show_choose_language:
        if _preferences.language is None:
            call choose_language
        $ persistent.has_chosen_language = True

    if not persistent.first_run:
        call disclaimer
        $ persistent.first_run = True

        scene white with Dissolve(0.5)

    $ config.allow_skipping = False

    show white
    play music config.main_menu_music
    show intro with dissolve_intro
    pausem 2.5
    hide intro with dissolve_intro
    show splash_warning _("This game is an unofficial fan game that is unaffiliated with Team Salvato.") with dissolve_intro
    pausem 1.5
    hide splash_warning with dissolve_intro
    pausem 0.5

    $ config.allow_skipping = True

    return

label disclaimer:
    ## You can edit this message but you MUST declare that your mod is 
    ## unaffiliated with Team Salvato, requires that the player must 
    ## finish DDLC before playing, has spoilers for DDLC, and where to 
    ## get DDLC's files."
    "[config.name!t] is a Doki Doki Literature Club fan mod that is not affiliated in any way with Team Salvato."
    "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
    "Game files for Doki Doki Literature Club are required to play this mod, and can be downloaded for free at {a=https://ddlc.moe}https://ddlc.moe{/a} or on Steam."

    menu:
        "By playing [config.name!t] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."
        "I agree.":
            pass

    return