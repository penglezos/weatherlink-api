# WeatherLink API tester

A simple WeatherLink API testing script to fetch data.

## Description

WeatherLink API Tester is a script based on Javascript designed to facilitate interaction and testing with the WeatherLink API, which is typically used to access weather data from Davis Instruments' WeatherLink system. This script's purpose is to streamline the process of sending API requests, receiving responses, and validating the retrieved data.

## Requirements

* Davis instruments weather station hardware
* API Key v2 from https://www.weatherlink.com/account

## Installation instructions

* Clone this repository:
```
git clone https://github.com/penglezos/weatherlink-api && cd weatherlink-api
```

### Javascript method

* Modify `index.html` with your WeatherLink API credentials and station ID:
```
const API_KEY = '';
const API_SECRET = '';
const STATION_ID = '';
```

* Open `index.html` with any preferred web browser

### Python method

* Modify `weatherlink.py` with your WeatherLink API credentials and station ID:
```
API_KEY = ""
API_SECRET = ""
STATION_ID = ""
```

* Execute the following command through terminal `python weatherlink.py`

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
