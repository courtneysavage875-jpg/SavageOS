import requests

def get_news():
    try:
        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=23d7db44b1d444eea8f948b29f1ea35d"
        r = requests.get(url).json()
        headline = r["articles"][0]["title"]
        return f"Top news: {headline}"
    except:
        return "News currently unavailable."
