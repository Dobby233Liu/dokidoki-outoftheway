## definitions.rpy

# This file defines important stuff for DDLC and your mod!

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
        return im.MatrixColor(im.MatrixColor(im.MatrixColor(path, im.matrix.desaturate() * im.matrix.contrast(contr)), 
            im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), im.matrix.desaturate() * im.matrix.colorize(blackCol, whiteCol))

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
image splash = "bg/splash.png"

# Characters Images
# This is where the characters bodies and faces are defined in the mod.
# They are defined by a left half, a right half and their head.
# To define a new image, declare a new image statement like in this example:
#     image sayori 1ca = Composite((960, 960), (0, 0), "mod_assets/sayori/1cl.png", (0, 0), "mod_assets/sayori/1cr.png", (0, 0), "sayori/a.png")

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

default persistent.playername = ""
default player = persistent.playername

default chapter = 0

# Names of the Characters
# To define a default name make a character name variable like in this example:
#   default e_name = "Eileen"