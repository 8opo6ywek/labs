from data_collection.openweathermap import get_weather_by_city, get_forecast_by_city
from data_collection.newsapi import get_top_headlines, get_everything_about_topic
from data_collection.coingecko import get_coin_list, get_coin_market_data
from database.mongo_utils import save_to_mongo

def main():
    # Weather data
    city = 'London'
    weather = get_weather_by_city(city)
    forecast = get_forecast_by_city(city)
    save_to_mongo('weather', weather)
    save_to_mongo('forecast', forecast)

    # News data
    top_headlines = get_top_headlines()
    save_to_mongo('news', top_headlines.get('articles', []))
    everything_about_python = get_everything_about_topic('Python')
    save_to_mongo('python_news', everything_about_python.get('articles', []))

    # Crypto data
    coin_list = get_coin_list()
    bitcoin_market_data = get_coin_market_data('bitcoin')
    save_to_mongo('crypto', coin_list)
    save_to_mongo('bitcoin_market', bitcoin_market_data)

if __name__ == "__main__":
    main()
