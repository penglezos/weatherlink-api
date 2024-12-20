import os
import requests
import json

# Your API v2 credentials
API_KEY = ""
API_SECRET = ""
STATION_ID = ""

# API v2 Endpoint URL (https://weatherlink.github.io/v2-api/api-reference)
ENDPOINT = "current"

# API v2 URL and headers
url = f"https://api.weatherlink.com/v2/{ENDPOINT}/{STATION_ID}"
headers = {
    "X-API-Key": API_KEY,
    "X-API-Secret": API_SECRET
}

# Make the GET request
response = requests.get(url, headers=headers)

# Print and save the response to a JSON file
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
    with open("weather_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Weather data saved to 'weather_data.json'")
else:
    print(f"Error: {response.status_code}, {response.text}")