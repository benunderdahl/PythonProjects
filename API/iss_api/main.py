import requests
from datetime import datetime
import time
from smtplib import SMTP

MY_LAT = 29.4252 # Your latitude
MY_LONG = -98.4946 # Your longitude
PORT = 587


def check_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset and time_now.hour <= sunrise:
        return True
    return False

#Your position is within +5 or -5 degrees of the ISS position.
def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT -5 <= iss_latitude <= MY_LAT + 5:
        return True
    return False

while True:
    if check_position() and check_night():
        email = ""
        password = ""
        with SMTP("smtp.gmail.com", PORT) as conn:
            conn.starttls()
            conn.login(email, password)
            conn.sendmail(email, "", msg="Subject: Look Up in the Sky\n\n The ISS is overhead right now")
    time.sleep(60)