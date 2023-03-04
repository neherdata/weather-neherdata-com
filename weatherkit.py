import datetime

# pip install requests PyJWT cryptography
import jwt
import requests

# https://developer.apple.com/account/resources/identifiers/list/serviceId
WEATHERKIT_SERVICE_ID = ""  # Create service like (use same ending): com.example.weatherkit-client

# https://developer.apple.com/account/  - click Membership in nav to get Team ID
WEATHERKIT_TEAM_ID = ""

# https://developer.apple.com/account/resources/authkeys/list
WEATHERKIT_KID = ""  # key ID
WEATHERKIT_KEY = ""  # contents of p8 file 

WEATHERKIT_FULL_ID = f"{WEATHERKIT_TEAM_ID}.{WEATHERKIT_SERVICE_ID}"

def fetch_weatherkit(
  lang="en",
  lat="29.8752",
  lon="-98.2625",
  country="US",
  timezone="US/Chicago",
  datasets = "currentWeather,forecastDaily,forecastHourly,forecastNextHour",
 ):
  url = f"https://weatherkit.apple.com/api/v1/weather/{lang}/{lat}/{lon}?dataSets={datasets}&countryCode={country}&timezone={timezone}"
  
  now = datetime.datetime.now(tz=datetime.timezone.utc)
  exp = now + datetime.timedelta(hours=1)

  token_body = {
    "sub": WEATHERKIT_SERVICE_ID,
    "iss": WEATHERKIT_TEAM_ID,
    "exp": exp,
    "iat": now
  }
  token_headers = {
    "kid": WEATHERKIT_KID,
    "id": WEATHERKIT_FULL_ID
  }
  token = jwt.encode(token_body, WEATHERKIT_KEY, headers=token_headers, algorithm="ES256")

  response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
  return response.json()
  