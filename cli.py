import os

def msgbox(title: str, text: list[str]):
    titlebar: str = ""
    titlebar += title
    contents: list[str] = []

    # resize window to biggest line
    if len(max(text)) + 4 > len(titlebar):
        while len(max(text)) + 4 > len(titlebar):
                titlebar = "═" + titlebar + "═"

    # add borders to and resize the contents
    for i in range(0, len(text)):
        txt: str = "║ " + text[i]
        if len(txt) < len(titlebar):
            while len(txt) < len(titlebar):
               txt += " "
        txt += " ║"
        contents.append(txt)

    # titlebar corners
    titlebar = "╔" + titlebar
    titlebar += "╗"

    width: int = len(titlebar)
    
    # bottom
    contents.append("╚" + ("═" * (width - 2)) + "╝")

    # outputs the box to screen
    print(titlebar.center(os.get_terminal_size()[0] - 1, " "))
    for i in range(0, len(contents)):
        print(contents[i].center(os.get_terminal_size()[0] - 1, " "))

def entry(title: str, text: list[str]):
    # basicaly the same as msg box - no comment

    titlebar: str = ""
    titlebar += title
    contents: list[str] = []

    if len(max(text)) + 4 > len(titlebar):
        while len(max(text)) + 4 > len(titlebar):
                titlebar = "═" + titlebar + "═"

    for i in range(0, len(text)):
        txt: str = "║ " + text[i]
        if len(txt) < len(titlebar):
            while len(txt) < len(titlebar):
               txt += " "
        txt += " ║"
        contents.append(txt)
    
    titlebar = "╔" + titlebar
    titlebar += "╗"

    width: int = len(titlebar)
    
    contents.append("╚" + ("═" * (width - 2)) + "╝")

    print(titlebar.center(os.get_terminal_size()[0] - 1, " "))
    for i in range(0, len(contents)):
        print(contents[i].center(os.get_terminal_size()[0] - 1, " "))

    print("═" * width)
    val = input()
    return val