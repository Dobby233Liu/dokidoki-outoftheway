## effects.rpy

# This file defines all the effects in this mod

init python:
    # This screenshot is used to screenshot the game which is used for different
    # effects in-game.
    def screenshot_srf():
        return renpy.display.draw.screenshot(None)