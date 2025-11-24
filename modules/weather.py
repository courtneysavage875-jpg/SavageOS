import requests

def get_weather():
    try:
        url = "https://wttr.in/Houston?format=%t,%w"
        data = requests.get(url).text
        temp, wind = data.split(",")
        return f"The weather in Houston is {temp} with wind {wind}."
    except:
        return "Weather data unavailable right now."


