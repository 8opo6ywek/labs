import requests
from config.config import API_KEYS
from app.models import normalize_weather_data

def get_weather_by_city(city):
    api_key = API_KEYS['openweathermap']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return normalize_weather_data(data)

def get_forecast_by_city(city):
    api_key = API_KEYS['openweathermap']
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data
