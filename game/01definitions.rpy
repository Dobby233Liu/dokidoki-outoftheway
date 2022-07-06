# 01definitions.rpy
# This file contains the definitions for some exceptions
# and imports certain Python modules at runtime
# and also defines some Creator Defined Statements

python early:
    # For effects
    import math

    # For credits
    import datetime

    # For path detection
    import os
    
    class DDLCRPAsMissing(Exception):
        def __init__(self, archive):
            self.archive = archive

        def __str__(self):
            return "'" + self.archive + ".rpa' was not found in the game folder. Check your DDLC installation for missing RPAs and try again."

    class IllegalModLocation(Exception):
        def __str__(self):
            return "DDLC mods/mod projects cannot be run from a cloud folder. Move your mod/mod project to another location and try again."

python early:
    def parse_pause_mine(lexer):
        return lexer.float()

    def execute_pause_mine(time):
        time = time and float(time) or None
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0.0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False

    def lint_pause_mine(time):
        if time and not isinstance(time, float):
            renpy.error(time)

    # With my edits you can now use pausem x.x
    # in place of $ pause(x.x) lmao
    renpy.register_statement(
        "pausem",
        parse=parse_pause_mine,
        execute=execute_pause_mine,
        lint=lint_pause_mine,
    )
