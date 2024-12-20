# WeatherLink API tester

A simple WeatherLink API testing script to fetch data.

## Description

WeatherLink API Tester is a Python script designed to facilitate interaction and testing with the WeatherLink API, which is typically used to access weather data from Davis Instruments' WeatherLink system. This script's purpose is to streamline the process of sending API requests, receiving responses, and validating the retrieved data.

## Requirements

* Davis instruments weather station hardware
* API Key v2 from https://www.weatherlink.com/account
* Python package installed

## Installation instructions

* Clone this repository:
```
git clone https://github.com/penglezos/weatherlink-api && cd weatherlink-api
```

* Modify `weatherlink.py` with your WeatherLink API credentials and station ID:
```
API_KEY = ""
API_SECRET = ""
STATION_ID = ""
```

* Execute the following command through terminal:

```
python weatherlink.py
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
