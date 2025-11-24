import os

def say(text):
    os.system(f'termux-tts-speak "{text}"')
