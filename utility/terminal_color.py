class TerminalColors:
    EXCAPE = '\033[{}m'

    COLORS = {
        'FOREGROUND': {
            'default': EXCAPE.format(39),
            'black': EXCAPE.format(30),
            'red': EXCAPE.format(31),
            'green': EXCAPE.format(32),
            'yellow': EXCAPE.format(33),
            'blue': EXCAPE.format(34),
            'magenta': EXCAPE.format(35),
            'cyan': EXCAPE.format(36),
            'light-gray': EXCAPE.format(37),
            'dark-gray': EXCAPE.format(90),
            'light-red': EXCAPE.format(91),
            'light-green': EXCAPE.format(92),
            'light-yellow': EXCAPE.format(93),
            'light-blue': EXCAPE.format(94),
            'light-magenta': EXCAPE.format(95),
            'light-cyan': EXCAPE.format(96),
            'white': EXCAPE.format(97),
        },
        'BACKGROUND': {
            'default': EXCAPE.format(49),
            'black': EXCAPE.format(40),
            'red': EXCAPE.format(41),
            'green': EXCAPE.format(42),
            'yellow': EXCAPE.format(43),
            'blue': EXCAPE.format(44),
            'magenta': EXCAPE.format(45),
            'cyan': EXCAPE.format(46),
            'light-gray': EXCAPE.format(47),
            'dark-gray': EXCAPE.format(100),
            'light-red': EXCAPE.format(101),
            'light-green': EXCAPE.format(102),
            'light-yellow': EXCAPE.format(103),
            'light-blue': EXCAPE.format(104),
            'light-magenta': EXCAPE.format(105),
            'light-cyan': EXCAPE.format(106),
            'white': EXCAPE.format(107),
        },
    }

    STYLES = {
        'bold': EXCAPE.format(1),
        'dim': EXCAPE.format(2),
        'underline': EXCAPE.format(4),
        'blink': EXCAPE.format(5),
        'reverse': EXCAPE.format(7),
        'hidden': EXCAPE.format(8),

        'RESET': {
            'all': EXCAPE.format(0),
            'bold': EXCAPE.format(21),
            'dim': EXCAPE.format(22),
            'underline': EXCAPE.format(24),
            'blink': EXCAPE.format(25),
            'reverse': EXCAPE.format(27),
            'hidden': EXCAPE.format(28),
        }
    }


HEADER = TerminalColors.COLORS['FOREGROUND']['light-magenta']

OKBLUE = TerminalColors.COLORS['FOREGROUND']['light-blue']
OKGREEN = TerminalColors.COLORS['FOREGROUND']['light-green']

WARNING = TerminalColors.COLORS['FOREGROUND']['light-yellow']
FAIL = TerminalColors.COLORS['FOREGROUND']['light-red']

END = TerminalColors.STYLES['RESET']['all']

BOLD = TerminalColors.STYLES['bold']
UNDERLINE = TerminalColors.STYLES['underline']
HIDE = TerminalColors.STYLES['hidden']
