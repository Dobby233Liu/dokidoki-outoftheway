## This mod is based on DDLC Mod Template version 4.0.0,
## Python 3/Ren'Py 8 variant.
# When asked to provide the version of the template you are using,
# provide this version number.

## options.rpy
# This file customizes what your mod is and and how it starts and builds!

# This controls what your mod is called.
define config.name = "DDLC Mod Template"

# Version number of your mod.
define config.version = "4.0.0–Py3"

# This control the name of your mod build when you package your mod.
# The build name is ASCII only so no numbers, spaces, or semicolons.
define build.name = "DDLCModTemplateTwo-Py3"

# Shows the sound volume slider.
define config.has_sound = True

# Shows the music volume slider.
define config.has_music = True

# Shows the voice volume slider.
define config.has_voice = True

# This configures what music will play when you launch your mod and in the 
# main menu.
define config.main_menu_music = audio.t1

# These variables control the transition effects of DDLC when entering and exiting
# a menu.
#   config.enter_transition controls the effect seen when entering the game menu.
#   config.exit_transition controls the effect when returning to the game.
#   Dissolve(X) dissolves the menu or last screen by X seconds.
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# This controls the transition effect of DDLC after loading the game.
define config.after_load_transition = None

# This controls the transition effect when your mod has reached the end of its' story.
define config.end_game_transition = Dissolve(.5)

# This controls the textbox that the characters use to speak.
#   "auto" sets the textbox to hide during scenes and show when a character speaks
#   "show" sets the textbox to show at all times
#   "hide" only shows dialogue when a character speaks.
define config.window = "auto"

# This controls the transition effects of the textbox.
#   config.window_show_transition controls the effect when the textbox is shown.
#   config.window_hide_transition controls the effect when the textbox is hidden.
#   Dissolve(X) dissolves the menu or last screen by X seconds.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# This sets the text speed of your mod.
default preferences.text_cps = 50

# This controls the auto-text forward speed of your mod.
default preferences.afm_time = 15

# This controls the audio level of your mod.
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# This controls whether the gamepad is enabled.
default preferences.pad_enabled = False

# This controls the save folder name of your mod.
# Finding your Saves:
#   Windows: %AppData%/RenPy/
#   macOS: $HOME/Library/RenPy/ (Un-hide the Library Folder)
#   Linux: $HOME/.renpy/
define config.save_directory = "DDLCModTemplateTwo-Py3"

# This controls the window logo of your mod.
define config.window_icon = "gui/window_icon.png"

# This controls whether your mod allows the player to skip dialogue.
define config.allow_skipping = True

# This controls whether your mod saves automatically.
define config.has_autosave = False

# This controls whether you mod saves automatically when quitting the game.
define config.autosave_on_quit = False

# This controls the number of slots auto-save can use for saving the game.
define config.autosave_slots = 0

# This controls whether the player can rollback to the previous dialogue in-game.
define config.rollback_enabled = config.developer

# These variables controls the layers placement of screens, images, and more. 
# It is highly recommended to leave these variables alone.
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

define config.atl_start_on_show = False

init python:
    # Replaces '--' or ' - ' in spoken dialogue
    # to U+2014 EM DASH.
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s

    config.replace_text = replace_text

    # Makes the game only allow opening the game menu
    # when quick menu is enabled.
    def game_menu_action():
        if not quick_menu:
            return
        renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_action

    # Allows only integer multiples of the original screen size
    # when the size of the physical window is changed.
    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

    config.adjust_view_size = force_integer_multiplier

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    ## The following variables take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##  * matches all characters, except the directory separator.
    ##  ** matches all characters, including the directory separator.
    ##
    ## Examples:
    ##  "*.txt" matches txt files in the base directory.
    ##  "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories.
    ##  "**.psd" matches psd files anywhere in the project.

    # This declares a package to build a IPG compliant distribution
    # of this mod.
    build.package("mod", 'zip', 'windows linux mac renpy',
        description="Ren'Py 8 DDLC Compliant Mod")

    # This declares the archives in the distribution.
    build.archive("scripts", 'mod')
    build.archive("mod_assets", 'mod')

    # Do not touch these lines. This is so Ren'Py adds a
    # Python launcher file for your mod and a special launcher
    # for Linux and macOS to run your mod. 
    try: 
        build.renpy_patterns.remove(('renpy.py', ['all']))
        build.classify_renpy("renpy.py", "renpy all")
    except: pass
    try:
        build.early_base_patterns.remove((config.name + '.sh', None))
        build.classify("LinuxLauncher.sh", "linux") ## Linux Launcher Script
        build.classify(config.name + ".sh", None)
    except: pass

    #############################################################
    # These variables classify files to add into the distribution.
    # Make sure to add 'all' to your build.classify variable if you are planning
    # to build your mod on Android like in this example.
    #   Example: build.classify("game/**.pdf", "scripts all")

    build.classify('game/audio.rpa', None)
    build.classify('game/images.rpa', None)
    build.classify('game/fonts.rpa', None)
    build.classify('**.rpy', None)
    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/tl/**", "scripts all")
    build.classify("game/**.rpyc", "scripts all")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)

    build.classify('README.html', 'mod all')
    build.classify('README.linux', 'linux')
   
    # This sets README.html as a documentation
    build.documentation('README.html')

    build.include_old_themes = False
