
import requests
import datetime as dt

LAT = 24.180221
LONG = 91.822259
TIMEZONE = "Asia/Kolkata"
FORMAT = 0

parameters = {
    "lat": LAT,
    "lng": LONG,
    "tzid": TIMEZONE,
    "formatted": FORMAT,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, )
response.raise_for_status()

sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

now = dt.datetime.now()

current_hour = now.hour

print(sunrise)
print(sunset)
print(current_hour)

