## definitions.rpy

# This file defines important stuff for DDLC and your mod!

python early:
    # This starts singleton to make sure only one copy of the mod
    # is running.
    import singleton
    me = singleton.SingleInstance()

# This python statement checks that 'audio.rpa', 'fonts.rpa' and 'images.rpa'
# are in the game folder and if the project is in a cloud folder (OneDrive).
# Note: For building a mod for PC/Android, you must keep the DDLC RPAs 
# and decompile them for the builds to work.
init -100 python:
    if not renpy.android:
        for archive in ['audio','images','fonts']:
            if archive not in config.archives:
                raise DDLCRPAsMissing(archive)

        if renpy.windows:
            onedrive_path = os.environ.get("OneDrive", None)
            if onedrive_path is not None and onedrive_path in config.basedir:
                raise IllegalModLocation

    # Limits the engine to only use one save location (user savedir)
    # See init function of savelocation.py in Ren'Py.
    if not config.developer and len(renpy.loadsave.location.locations) > 1:
        renpy.loadsave.location.locations = renpy.loadsave.location.locations[:1]

## Music
# This section declares the music available to be played in the mod.
# Syntax:
#   audio. - This tells Ren'Py this is a audio variable.
#   t1 - This tells Ren'Py the label of the music/sound file being declared.
#   <loop 22.073> - This tells Ren'Py to loop the music/sound to this position when the song completes.
#   "bgm/1.ogg" - This tells Ren'Py the path of the music/sound file to use.
# Example: 
#   define audio.t2 = "bgm/2.ogg"

define audio.t1 = "<loop 22.073>bgm/1.ogg" # Doki Doki Literature Club! - Main Theme

## Backgrounds
# This section declares the backgrounds available to be shown in the mod.
# To define a new color background, declare a new image statement like in this example:
#     image blue = "X" where X is your color hex i.e. '#158353'
# To define a new background, declare a new image statement like this instead:
#     image bg bathroom = "mod_assets/bathroom.png" 

image black = "#000000"
image white = "#ffffff"

## Team Salvato Splash Screen
# This image stores the Tean Salvato logo image that appears when the game starts.
image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with dissolve_intro
    2.5
    "white" with dissolve_intro
    0.5

# Image text for the splash message when the game loads.
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

## Main Menu Images
# These image transforms store the images and positions of the game logo,
# the menu character sprites and main menu/pause menu screen images.

# This image shows the DDLC logo in the normal DDLC position.
image menu_logo:
    "mod_assets/DDLCModTemplateLogo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

# This image shows the main menu polka-dot image.
image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

# This image shows the pause menu polka-dot image.
image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

# This image transform shows the white fading effect in the main menu.
image menu_fade:
    "white"
    menu_fadeout

# This image shows the main menu screen in the main/pause menu.
image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

## Main Menu Effects
# These transforms and image transform store the effects that appear in the
# main menu on startup.

# This image transform shows a particle burst effect image to the main menu when
# the game starts.
image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explode_time=0, particles_num=40, total_time=2.0, x_speed=3, y_speed=3).sm
    particle_fadeout

# Characters Images
# This is where the characters bodies and faces are defined in the mod.
# They are defined by a left half, a right half and their head.
# To define a new image, declare a new image statement like in this example:
#     image sayori 1ca = Composite((960, 960), (0, 0), "mod_assets/sayori/1cl.png", (0, 0), "mod_assets/sayori/1cr.png", (0, 0), "sayori/a.png")


# Names of the Characters
# To define a default name make a character name variable like in this example:
#   default e_name = "Eileen"


## Character Variables
# This is where the characters are declared in the mod.
# To define a new character with assets, declare a character variable like in this example:
#   define e = DynamicCharacter('e_name', image='eileen', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
# To define a new character without assets, declare a character variable like this instead:
#   define en = Character('Also eileen lmao', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

## Variables
# This section declares variables when the mod runs for the first time on all saves.
# To make a new persistent variable, make a new variable with the 'persistent.' in it's name
# like in this example:
#   default persistent.monika = 1
# To make a non-persistent variable, make a new variable like this instead:
#   default cookies = False
# To make sure a variable is set to a given condition use 'define' rather than 'default'.

## This sets the first run variable to False to show the disclaimer.
default persistent.first_run = False
## This sets the persistent to false in order to choose a language.
default persistent.has_chosen_language = False

default persistent.playername = ""
default player = persistent.playername

define allow_skipping = True

default chapter = 0

# This init python statement sets up Python functions
# for the game.
init python:
    global _windows_hidden
    _windows_hidden = False

    """
    This function gets the postition of the music playing in a given channel.
    """
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    """
    This recolor function allows you to recolor the GUI of DDLC easily without replacing
    the in-game assets. Introduced in version 3.0.0 of the mod template.

    Syntax to use:
        recolorize("path/to/your/image", "#color1hex", "#color2hex", contrast value)
    Example:
        recolorize("gui/menu_bg.png", "#bdfdff", "#e6ffff", 1.25)
    """
    def recolorize(path, blackCol="#ffbde1", whiteCol="#ffe6f4", contr=1.29):
        return im.MatrixColor(
            im.MatrixColor(
                im.MatrixColor(path, im.matrix.desaturate() * im.matrix.contrast(contr)),
                im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)
            ),
            im.matrix.desaturate() * im.matrix.colorize(blackCol, whiteCol)
        )

    def set_allow_skipping(allow):
        allow_skipping = allow
        config.allow_skipping = allow
        return allow

label after_load:
    # Load skipping toggle state saved in the save
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ style.say_dialogue = style.normal
    return