import requests
from datetime import *
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Getting dates
if datetime.now().weekday() == 6:
    yesterday = date.today() - timedelta(days=2)
    day_before = date.today() - timedelta(days=3)
elif datetime.now().weekday() == 0:
    yesterday = date.today() - timedelta(days=3)
    day_before = date.today() - timedelta(days=4)
elif datetime.now().weekday() == 1:
    yesterday = date.today() - timedelta(days=1)
    day_before = date.today() - timedelta(days=4)
else:
    yesterday = date.today() - timedelta(days=1)
    day_before = date.today() - timedelta(days=2)

yesterday = yesterday.strftime("%Y-%m-%d")
day_before = day_before.strftime("%Y-%m-%d")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_key = os.getenv("ALPHA_VANTAGE_KEY")
stock_site = "https://www.alphavantage.co/query?"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_key
}

stock_response = requests.get(stock_site, params=stock_params)
data = stock_response.json()
y_price = float(data["Time Series (Daily)"][yesterday]["4. close"])
db_price = float(data["Time Series (Daily)"][day_before]["4. close"])

change = (y_price - db_price) / db_price
if abs(change) >= .1:
    up_down = "🔻"
    if change > 0:
        up_down = "🔺"

    news_key = os.getenv("NEWS_API_KEY")
    news_site = "https://newsapi.org/v2/everything?"
    news_params = {
        "q": COMPANY_NAME,
        "from": day_before,
        "to": yesterday,
        "sortBy": "popularity",
        "apiKey": news_key
    }

    news_response = requests.get(news_site, params=news_params)
    data = news_response.json()
    articles = [data["articles"][0], data["articles"][1], data["articles"][2]]

    articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in articles]

    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN")
    )
    for article in articles:
        message = client.messages.create(
            body=f"{STOCK}: {up_down}{abs(change)}\n"+article,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=os.getenv("TARGET_PHONE_NUMBER")
        )
else:
    print(f"{STOCK} is currently a stagnant stock")
