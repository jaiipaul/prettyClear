import random


class Color:
    def __init__(self, name: str, code: str):
        self._name = name
        self._code = code

    def __add__(self, other: str):
        return self._code+other

    def __repr__(self):
        return self._code

    @property
    def name(self) -> str:
        return self._name

    @property
    def code(self) -> str:
        return self._code


class TerminalColors:
    reset = '\x1b[0m'
    bold = '\x1b[01m'
    disable = '\x1b[02m'
    underline = '\x1b[04m'
    reverse = '\x1b[07m'
    strikethrough = '\x1b[09m'
    invisible = '\x1b[08m'

    class fg:
        black = Color('black', '\x1b[30m')
        red = Color('red', '\x1b[31m')
        green = Color('green', '\x1b[32m')
        yellow = Color('yellow', '\x1b[33m')
        blue = Color('blue', '\x1b[34m')
        magenta = Color('magenta', '\x1b[35m')
        cyan = Color('cyan', '\x1b[36m')
        white = Color('white', '\x1b[37m')
        _COLORS = [black, red, green, yellow, blue, magenta, cyan, white]

        @staticmethod
        def register(name: str, red: int, green: int, blue: int):
            if hasattr(TerminalColors.fg, name):
                return
            new_color = Color(name, f'\x1b[38;2;{red};{green};{blue}m')
            setattr(TerminalColors.fg, name, new_color)
            TerminalColors.fg._COLORS.append(new_color)

        def get_colors(self) -> list[Color]:
            return TerminalColors.bg._COLORS

        @staticmethod
        def random() -> Color:
            n_colors = len(TerminalColors.fg._COLORS)
            return TerminalColors.bg._COLORS[random.randint(0, n_colors-1)]

    class bg:
        black = Color('black', '\x1b[40m')
        red = Color('red', '\x1b[41m')
        green = Color('green', '\x1b[42m')
        yellow = Color('yellow', '\x1b[43m') 
        blue = Color('blue', '\x1b[44m')
        magenta = Color('magenta', '\x1b[45m')
        cyan = Color('cyan', '\x1b[46m')
        white = Color('white', '\x1b[47m')
        _COLORS = [black, red, green, yellow, blue, magenta, cyan, white]

        @staticmethod
        def register(name: str, red: int, green: int, blue: int):
            if hasattr(TerminalColors.bg, name):
                return
            new_color = Color(name, f'\x1b[48;2;{red};{green};{blue}m')
            setattr(TerminalColors.bg, name, new_color)
            TerminalColors.bg._COLORS.append(new_color)

        def get_colors(self) -> list[Color]:
            return TerminalColors.bg._COLORS

        @staticmethod
        def random() -> Color:
            n_colors = len(TerminalColors.bg._COLORS)
            return TerminalColors.bg._COLORS[random.randint(0, n_colors-1)]
