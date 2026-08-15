
import requests
import datetime as dt

my_lat = 24.197914
my_lng = 91.835580
my_time_format = 0
my_timezone = "Asia/Kolkata"


parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": my_time_format,
    "tzid": my_timezone
}

#? My Sunrise Sunset Time
sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()
sun_data = sun_response.json()

sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

print(f"Sunrise Time: {sunrise}")
print(f"Sunset Time: {sunset}")

#? My Current Time
current_time = dt.datetime.now().hour
print(f"My Current Time: {current_time}")

#? ISS Latitude Longitude
iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()

iss_lat = float(iss_data["iss_position"]["latitude"])
iss_lng = float(iss_data["iss_position"]["longitude"])

print(f"ISS Latitude: {iss_lat} | My Latitude: {my_lat}")
print(f"ISS Longitude: {iss_lng} | My Longitude: {my_lng}")

def track_lat():
    if iss_lat - my_lat <= 3 or my_lat - iss_lat <= 3:
        return True

def track_lng():
    if iss_lng - my_lng <= 3 or my_lng - iss_lng <= 3:
        return True

def send_email():
    print("Email Sent")

def track_iss():
    if track_lat() and track_lng():
        send_email()

if current_time <= sunrise or current_time >= sunset:
    track_iss()
    
