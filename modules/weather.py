import requests

def get_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=29.7604&longitude=-95.3698&current_weather=true"
        r = requests.get(url, timeout=5)
        data = r.json()
        weather = data["current_weather"]

        temp = weather["temperature"]
        wind = weather["windspeed"]

        return f"The weather in Houston is {temp}°F with wind at {wind} mph."
    except:
        return "Weather data unavailable right now."
