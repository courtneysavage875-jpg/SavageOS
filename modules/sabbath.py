from datetime import datetime, timedelta
from astral.sun import sun
from astral import LocationInfo
import pytz

houston = LocationInfo("Houston", "USA", "America/Chicago", 29.7604, -95.3698)

def is_sabbath_now():
    s = sun(houston.observer, date=datetime.now(pytz.timezone("America/Chicago")))

    friday_sunset = s["sunset"]
    saturday_sunset = friday_sunset + timedelta(days=1)

    now = datetime.now(pytz.timezone("America/Chicago"))

    return friday_sunset <= now <= saturday_sunset
