import pyautogui


def do_stuff():
    pyautogui.sleep(5)
    pyautogui.typewrite(["a", "space", "b", "enter"], 0.25)
    pyautogui.typewrite("I am not a robot!", 0.25)
    pyautogui.hotkey("ctrl", "c")


if __name__ == '__main__':
    do_stuff()
