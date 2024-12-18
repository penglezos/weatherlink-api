import requests
import hashlib
import time
import json  # Module to handle JSON data

# Your API credentials
API_KEY = ""
API_SECRET = ""
STATION_ID = ""

# API URL and headers
url = f"https://api.weatherlink.com/v2/current/{STATION_ID}"
headers = {
    "X-API-Key": API_KEY,
    "X-API-Secret": API_SECRET
}

# Make the GET request
response = requests.get(url, headers=headers)

# Save the response to a JSON file
if response.status_code == 200:
    data = response.json()  # Parse response as JSON
    # Save the data to a file
    with open("weather_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)  # Save with indentation for readability
    print("Weather data saved to 'weather_data.json'")
else:
    print(f"Error: {response.status_code}, {response.text}")