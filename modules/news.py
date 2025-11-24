import requests

def get_news():
    try:
        url = "https://api.currentsapi.services/v1/latest-news?language=en"
        r = requests.get(url, timeout=5)
        data = r.json()

        articles = data.get("news", [])[:3]
        headlines = [a["title"] for a in articles]

        return "Top news: " + " | ".join(headlines)
    except:
        return "News unavailable right now."
