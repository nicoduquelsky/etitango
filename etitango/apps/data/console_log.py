"""
    Pocket Console log for Python
    creator: @schrottgerardo
    repository: https://github.com/schrottgerardo/Pocket-Console-Log-for-python
    Version: 1.0

    1) Add this line to your .py file:
        import console_log.py
    2) call "run", "err" or "warn" methods
    Optional: you can bold your *args too
"""

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'

    """
        If you want to add background colors too,
        here is a example of how could be.
    """
    # class bg:
    #     black='\033[40m'
    #     red='\033[41m'
    #     green='\033[42m'
    #     orange='\033[43m'
    #     blue='\033[44m'
    #     purple='\033[45m'
    #     cyan='\033[46m'
    #     lightgrey='\033[47m'


cg = colors.fg.green
cr = colors.fg.red
cw = colors.fg.lightgrey
tt = colors.fg.purple + colors.bold
cb = colors.bold
c = colors.reset
OK = cw+"["+cg+cb+"running"+c+cw+"]"+cw+cb+" "
AST = cw+"["+tt+"warning"+c+cw+"]"+cw+cb+" "
ERR = cw+"["+cr+cb+"error"+c+cw+"]"+cw+cb+" "

def run(self, *args):
    text = str(self)
    for bold in args:
        bold = str(bold)
        new_bold = tt+bold+c+cw+cb
        text = text.replace(bold, new_bold)
    print("\n"+OK+text+c+"\n")

def warn(self, *args):
    text = str(self)
    for bold in args:
        bold = str(bold)
        new_bold = tt+bold+c+cw+cb
        text = text.replace(bold, new_bold)
    print("\n"+AST+text+c+"\n")

def err(self, *args):
    text = str(self)
    for bold in args:
        bold = str(bold)
        new_bold = tt+bold+c+cw+cb
        text = text.replace(bold, new_bold)
    print("\n"+ERR+text+c+"\n")
