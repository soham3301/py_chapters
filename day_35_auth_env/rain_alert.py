
import requests
import json
import os

KEY = os.environ.get("OWM_API_KEY")
print(KEY)
LAT = 24.19787
LON =  91.83489
UNIT = "metric"

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": KEY,
    "units": UNIT
}

#? CURRENT WEATHER
# current_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={KEY}&units=metric")
# current_response.raise_for_status()
# current_data = current_response.json()

# print(current_data)

#? 5 Day - 3 Hour Forecast
five_day_response = requests.get(API_ENDPOINT, params=weather_params)
five_day_response.raise_for_status()
five_day_data = five_day_response.json()["list"]

data_for_save = {}

# for item in five_day_data:
#     data_for_save[item["dt_txt"]] = item["main"]
#     #? Checking next 12 hrs rain data

twelve_hr_counter = 0
for rain in five_day_data:
    if rain["weather"][0]["main"] == "Rain":
        rain_time = rain["dt_txt"].split(" ")[1]
        rain_date = rain["dt_txt"].split(" ")[0]
        print(f"It will rain at: {rain_time} hrs on {rain_date}")
    twelve_hr_counter += 1
    if twelve_hr_counter > 5:
        break

def data_writer():
    with open("./weather_data_five_day.json", mode="w") as weather_file:
        json.dump(data_for_save, weather_file, indent=4)
