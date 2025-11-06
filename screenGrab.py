import PIL
import pyautogui
import time

def get_rows():
    time.sleep(3)
    whole_board = pyautogui.screenshot(region=(584,219, 884-584, 576-219))
    whole_board.save("images/whole_board.png")
    # region: left, top, width, height
    # top left of board x584 y219
    # bottom right of board x884 y576



get_rows()
# time.sleep(3)
# print(pyautogui.position())