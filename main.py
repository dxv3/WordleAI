from PIL import Image
import pyautogui
import time
from screenGrab import get_rows

with open("words.txt") as f:
    word_list = [line.strip().upper() for line in f if line.strip()]

def get_tile_colour(image_path):
    img = Image.open(image_path).convert("RGB")
    r, g, b = img.getpixel((10, 10))
    if (r, g, b) == (33, 42, 69):
        return "grey"
    elif (r, g, b) == (178, 157, 85):
        return "yellow"
    elif (r, g, b) == (80, 152, 109):
        return "green"
    return "unknown"

def update_guesses(row_index):
    guesses = ["", "", "", "", ""]
    for j in range(5):
        path = f"images/rows/row{row_index+1}_letter{j+1}.png"
        colour = get_tile_colour(path)
        if colour == "green":
            guesses[j] = "X"
        elif colour == "yellow":
            guesses[j] = "x"
        elif colour == "grey":
            guesses[j] = ""
    return guesses

def filter_words(words, guess, feedback):
    filtered = []
    for word in words:
        valid = True
        for i in range(5):
            letter = guess[i]
            result = feedback[i]

            if result == "X":  # green
                if word[i] != letter:
                    valid = False
                    break

            elif result == "x":  # yellow
                # must exist somewhere else, not same spot
                if letter not in word or word[i] == letter:
                    valid = False
                    break

            elif result == "":  # grey
                # only rule out if letter isn’t green/yellow elsewhere in guess
                if letter not in [g for g, f in zip(guess, feedback) if f in ("X", "x")] and letter in word:
                    valid = False
                    break

        if valid:
            filtered.append(word)
    return filtered



def guess_word():
    words = word_list[:]
    guess = "CRANE"

    for i in range(6):
        print(f"Attempt {i+1}: {guess}")
        pyautogui.typewrite(guess.lower())
        pyautogui.press("enter")
        time.sleep(2)

        get_rows()
        fb = update_guesses(i)
        print(f"Feedback: {fb}")

        if fb == ["X", "X", "X", "X", "X"]:
            print("Solved.")
            return

        words = filter_words(words, guess, fb)
        print(f"{len(words)} words left")

        if not words:
            print("No valid words left.")
            return

        guess = words[0]

    print("Failed to solve in 6 guesses.")

guess_word()
