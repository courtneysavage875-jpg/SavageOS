import json
from modules.weather import get_weather
from modules.news import get_news
from modules.speech import say
from modules.listener import listen
from modules.commands import handle_command
from modules.sabbath import is_sabbath_now
from modules.personality import greet_savage, sabbath_greeting

def boot():
    with open("assets/config.json") as f:
        config = json.load(f)

    say("SavageOS v2 booting up.")
    
    if config["sabbath_greeting"] and is_sabbath_now():
        say(sabbath_greeting())
    else:
        say(greet_savage())

    say("Checking weather.")
    say(get_weather())

    say("Checking news.")
    say(get_news())

    say("Boot sequence complete.")

    listen_for_commands()

def listen_for_commands():
    say("Awaiting your command, Savage.")
    while True:
        voice = listen()
        if voice:
            say(handle_command(voice))

if __name__ == "__main__":
    boot()
