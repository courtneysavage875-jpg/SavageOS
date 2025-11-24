import os

def listen():
    os.system("termux-speech-to-text > voice.txt")
    with open("voice.txt") as f:
        return f.read().lower().strip()
