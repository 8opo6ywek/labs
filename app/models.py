def normalize_weather_data(data):
    # Нормализация данных о погоде
    normalized_data = {
        "city": data.get("name"),
        "temperature": data.get("main", {}).get("temp"),
        "weather": data.get("weather", [{}])[0].get("description"),
    }
    return normalized_data

def normalize_news_data(data):
    # Нормализация данных о новостях
    normalized_data = {
        "title": data.get("title"),
        "description": data.get("description"),
        "url": data.get("url"),
        "published_at": data.get("publishedAt")
    }
    return normalized_data

def normalize_crypto_data(data):
    # Нормализация данных о криптовалюте
    normalized_data = {
        "id": data.get("id"),
        "symbol": data.get("symbol"),
        "name": data.get("name"),
        "current_price": data.get("market_data", {}).get("current_price", {}).get("usd"),
    }
    return normalized_data
