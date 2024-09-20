from flask import request, jsonify
from app import app, mongo
from app.utils import convert_objectid


@app.route('/api/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400

    weather_data = mongo.db.weather.find_one({"city": city})
    if not weather_data:
        return jsonify({"error": "No data found for the specified city"}), 404

    weather_data = convert_objectid(weather_data)  # Преобразуем ObjectId перед отправкой данных
    return jsonify(weather_data), 200


@app.route('/api/news', methods=['GET'])
def get_news():
    topic = request.args.get('topic')
    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    news_data = mongo.db.news.find({"description": {"$regex": topic, "$options": "i"}})
    news_list = list(news_data)

    if not news_list:
        return jsonify({"error": "No news found for the specified topic"}), 404

    news_list = convert_objectid(news_list)  # Преобразуем ObjectId перед отправкой данных
    return jsonify(news_list), 200


@app.route('/api/crypto', methods=['GET'])
def get_crypto():
    coin = request.args.get('coin')
    if not coin:
        return jsonify({"error": "Coin is required"}), 400

    crypto_data = mongo.db.crypto.find_one({"id": coin})
    if not crypto_data:
        return jsonify({"error": "No data found for the specified coin"}), 404

    crypto_data = convert_objectid(crypto_data)  # Преобразуем ObjectId перед отправкой данных
    return jsonify(crypto_data), 200