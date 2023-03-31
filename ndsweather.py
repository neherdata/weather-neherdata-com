# ndsweather.py

import os
import json
import weatherkit

# Load the credentials from wherever you store them securely
# team_id = os.environ.get('APPLE_TEAM_ID')
# key_id = os.environ.get('APPLE_KEY_ID')
# service_id = os.environ.get('APPLE_SERVICE_ID')
# private_key = os.environ.get('APPLE_PRIVATE_KEY')

keyfile = open("AuthKey_84FS6668BX.p8", "r")
keystring = keyfile.read()

team_id = "7QAM3LGSSC"
key_id = "84FS6668BX"
service_id = "com.neherdata.weather"
private_key = keystring

# Instantiate the WeatherKit object
wk_client = weatherkit.WeatherKit(team_id, service_id, private_key, key_id)

# Include any/all of the datasets we want to pull in the list
datasets = [
    "forecastHourly",
    "forecastDaily",
    "currentWeather",
    "forecastNextHour",
]

# Fetch the API
# forecasts = wk_client.fetch(datasets, 40.308392, -74.069771, "US", "US/Eastern")
secretariat = wk_client.fetch(datasets, 40.308392, -74.069771, "US", "US/Eastern")

# There is a convenience method for converting the forecast response object to JSON
secretariat_return = secretariat.as_json()
# secretariat_json = json.dumps(secretariat_return, indent=4)

with open("secretariat_weather.json", "w") as outfile:
    outfile.write(secretariat_return)

print(secretariat_return)
print(
    "Weather Data - Copyright © 2023 Apple Inc. All rights reserved. Apple Weather and Weather are trademarks of Apple Inc."
)
