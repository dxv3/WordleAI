from PIL import Image
import pyautogui
from screenGrab import get_rows

with open("words.txt") as f:
    words = [line.strip() for line in f if line.strip()]

def get_tile_colour(image_path):
    img = Image.open(image_path).convert("RGB")
    r,g,b = img.getpixel((10, 10))
    # grey 33,42,69
    if r==33 and g==42 and b==69:
        return "grey"
    # yellow 178,157,65
    elif r==178 and g==157 and b==85:
        return "yellow"
    # green 80,152,109
    elif r==80 and g==152 and b==109:
        return "green"

def update_guesses():
    guesses = [["", "", "", "", "",],
           ["", "", "", "", "",],
           ["", "", "", "", "",],
           ["", "", "", "", "",],
           ["", "", "", "", "",],
           ["", "", "", "", "",]
           ]
    for i in range(6):
        for j in range(5):
            path = f"images/rows/row{i+1}_letter{j+1}.png"
            colour = get_tile_colour(path)
            if colour == "green":
                guesses[i][j] = "X"
            elif colour == "yellow":
                guesses[i][j] = "x"
            elif colour == "grey":
                guesses[i][j] = ""
    return guesses
get_rows()
print(update_guesses())
