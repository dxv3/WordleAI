

with open("words.txt") as f:
    words = [line.strip() for line in f if line.strip()]

print(words[14854])