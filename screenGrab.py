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

    row_height = 357//6
    # get each row
    for i in range(6):
        top = 219+i*row_height
        bottom = top + row_height
        row_img = whole_board.crop((0, i * row_height, 300, (i+1)*row_height))
        row_img.save(f"images/rows/row_{i+1}.png")




get_rows()
# time.sleep(3)
# print(pyautogui.position())