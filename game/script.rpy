## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story! 

label start:

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below: 
    #   $ mi_name = "Mike". 
    # Don't forget to add the character to 'definitions.rpy'!

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    $ style.say_dialogue = style.normal
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ config.allow_skipping = True

    ## The Main Part of the Script

    "Nothing here, move along."

    return
