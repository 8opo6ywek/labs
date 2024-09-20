import requests
from config.config import API_KEYS

def get_top_headlines():
    api_key = API_KEYS['newsapi']
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json()

def get_everything_about_topic(topic):
    api_key = API_KEYS['newsapi']
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    response = requests.get(url)
    return response.json()
