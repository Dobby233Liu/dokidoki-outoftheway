## script.rpy

# This is the label that Ren'Py calls to start
# your mod's story!
label start:

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    $ style.say_dialogue = style.normal

    # These variables controls whether the player can skip dialogue or transitions.
    $ config.allow_skipping = True

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    # This variable sets the chapter variable to 0.
    $ chapter = 0

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below: 
    #   $ mi_name = "Mike". 
    # Don't forget to add the character to 'definitions.rpy'!

    ## The Main Part of the Script

    "Nothing here, move along."

    return
