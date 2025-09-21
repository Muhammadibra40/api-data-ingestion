import requests 
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = "London"
params = {
    "q": city,
    "appid": WEATHER_API_KEY,
    "units": "metric" 
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in {data['name']}, {data['sys']['country']}:")
    print(f"🌡 Temp: {data['main']['temp']}°C")
    print(f"☁ Condition: {data['weather'][0]['description']}")
    print(f"💨 Wind: {data['wind']['speed']} m/s")
else:
    print("Error:", response.status_code, response.text)