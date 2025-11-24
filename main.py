from modules.weather import get_weather
from modules.news import get_news
def boot():
    print("SavageOS v1 initialized\n")

    # Weather
    print("Checking weather...")
    print(get_weather())
    print("")

    # News
    print("Checking news...")
    print(get_news())
    print("")

    print("Boot sequence complete.")

if __name__ == "__main__":
    boot()
