python early:
    def parse_pause_mine(lexer):
        return lexer.float()

    def execute_pause_mine(time):
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False

    def lint_pause_mine(time):
        if not isinstance(time, float):
            renpy.error(tte)

    renpy.register_statement(
        "pausem",
        parse=parse_pause_mine,
        execute=execute_pause_mine,
        lint=lint_pause_mine,
    )