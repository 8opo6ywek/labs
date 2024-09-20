import requests

def get_coin_list():
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    return response.json()

def get_coin_market_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days=1"
    response = requests.get(url)
    return response.json()
