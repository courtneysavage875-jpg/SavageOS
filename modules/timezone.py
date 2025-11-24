import pytz
from datetime import datetime

def current_time():
    tz = pytz.timezone("America/Chicago")
    return datetime.now(tz).strftime("%A %I:%M %p")
