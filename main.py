import time
import pyautogui
from screenGrab import get_rows
from PIL import Image

with open("words.txt") as f:
    word_list = [line.strip() for line in f if line.strip()]

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
    guesses = [""] * 5
    for j in range(5):
        path = f"images/rows/row_{row_index+1}_letter{j+1}.png"
        colour = get_tile_colour(path)
        if colour == "green":
            guesses[j] = "X"
        elif colour == "yellow":
            guesses[j] = "x"
        elif colour == "grey":
            guesses[j] = ""
    return guesses

def filter_words(word_list, guess, feedback):
    filtered = []
    for word in word_list:
        valid = True
        for i, mark in enumerate(feedback):
            letter = guess[i]
            if mark == "X":  # green
                if word[i] != letter:
                    valid = False
                    break
            elif mark == "x":  # yellow
                if letter not in word or word[i] == letter:
                    valid = False
                    break
            elif mark == "":  # grey
                # only reject if letter isn't marked yellow/green elsewhere
                if letter not in [g for g, f in zip(guess, feedback) if f in ("X", "x")] and letter in word:
                    valid = False
                    break
        if valid:
            filtered.append(word)
    return filtered


def play_wordle():
    time.sleep(3)
    current_list = word_list[:]
    current_guess = "CRANE"

    for attempt in range(6):
        pyautogui.typewrite(current_guess.lower())
        pyautogui.press("enter")
        time.sleep(2)

        get_rows()  # capture new board
        feedback = update_guesses(attempt)
        print(f"Attempt {attempt+1}: {current_guess} -> {feedback}")

        if feedback == ["X", "X", "X", "X", "X"]:
            print("Solved.")
            return

        current_list = filter_words(current_list, current_guess, feedback)
        if not current_list:
            print("No valid words left.")
            return

        current_guess = current_list[0]  # simplest next guess

    print("Failed to solve in 6 guesses.")

play_wordle()