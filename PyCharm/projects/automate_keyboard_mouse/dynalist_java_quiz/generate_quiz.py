import pyautogui


def generate_quiz(start: int, end: int):
    """
    This function generates quiz templates for Dynalist for learning Java. I have a book with
    many quiz questions and I like it. I want to keep track of my answers in Dynalist. This template
    allows me to answer the questions with using ony the mouse. ^-^

    :param start: starting number
    :param end: finishing number
    :return:
    """
    pyautogui.sleep(7)
    for num in range(start, end+1):
        # input current number
        pyautogui.typewrite(str(num), interval=0.1)
        # next line and indent
        pyautogui.typewrite(["enter", "tab"], interval=0.1)
        pyautogui.typewrite("yay nay", interval=0.1)
        # make checked by ctrl+shift+c
        pyautogui.hotkey("ctrl", "shift", "c")
        pyautogui.typewrite(["enter",
                             "tab",
                             *list("yay"), "enter",
                             *list("nay"), "enter",
                             "A", "enter",
                             "B", "enter",
                             "C", "enter",
                             "D"
                             ], interval=0.1)
        # go back to base level
        pyautogui.typewrite(["enter"], interval=0.1)
        pyautogui.hotkey("shift", "tab")
        pyautogui.hotkey("shift", "tab")


if __name__ == '__main__':
    generate_quiz(6, 20)
