# Data Collection Project

## Описание

Этот проект собирает данные с нескольких публичных API и веб-сайтов, а затем сохраняет их в базу данных MongoDB. Он использует API для получения данных о погоде, криптовалютах и новостях, а также парсит данные с двух веб-страниц. Полученные данные сохраняются в MongoDB для дальнейшего анализа.

### Модули:

- **/api** — содержит модули для взаимодействия с публичными API:
  - `openweather.py`: получение данных о погоде из OpenWeatherMap.
  - `coingecko.py`: получение данных о криптовалютах из CoinGecko.
  - `newsapi.py`: получение новостей с NewsAPI.
  
- **/parsers** — модули для парсинга веб-страниц:
  - `crypto_news_parser.py`: парсинг новостей о криптовалютах с сайта CoinDesk.
  - `general_news_parser.py`: парсинг новостей с общего новостного сайта BBC.

- **/db** — модуль для взаимодействия с MongoDB:
  - `mongo_db.py`: функции для сохранения данных в MongoDB.

## Конфигурация

Для использования API OpenWeatherMap и NewsAPI необходимо добавить ваши ключи API в файлы:

- **/api/openweather.py**: замените `your_openweathermap_api_key` на ваш API ключ.
- **/api/newsapi.py**: замените `your_newsapi_key` на ваш API ключ.

## Зависимости

- `requests` — для работы с HTTP-запросами к API.
- `beautifulsoup4` — для парсинга веб-страниц.
- `pymongo` — для взаимодействия с MongoDB.

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.
