from modules.weather import get_weather
from modules.news import get_news
from modules.system import shutdown, update_system

def handle_command(voice):
    if "weather" in voice:
        return get_weather()

    if "news" in voice:
        return get_news()

    if "update" in voice:
        return update_system()

    if "shut down" in voice or "shutdown" in voice:
        return shutdown()

    return "I did not understand that command, Savage."
