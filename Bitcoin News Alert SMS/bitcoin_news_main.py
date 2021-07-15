import requests
import datetime
from newsapi import NewsApiClient
from twilio.rest import Client

ALPHAADVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = ""
NEWSAPI_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWSAPI_API_KEY = ""
account_sid = ""
auth_token = ""

SYMBOL = "BTC"
CRYPTO_NAME = "Bitcoin"

"""
Get CRYPTO price change in previous day.
"""
alphaadvantage_parameters = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": SYMBOL,
    "market": "USD",
    "apikey": ALPHAVANTAGE_API_KEY,
}

response = requests.get(ALPHAADVANTAGE_ENDPOINT, params=alphaadvantage_parameters)
print(response.status_code)
response.raise_for_status()
price_data = response.json()

# yesterday's date (%Y-%m-%d)
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
yesterday = datetime.datetime.strftime(yesterday, '%Y-%m-%d')

# get yesterday's price change
open = float(price_data["Time Series (Digital Currency Daily)"][yesterday]["1a. open (USD)"])
close = float(price_data["Time Series (Digital Currency Daily)"][yesterday]["4a. close (USD)"])
pct_change = round(((close-open)/open)*100, 2)

if pct_change > 0:
    arrow_emoji = "🔼"
else:
    arrow_emoji = "🔽"

if pct_change > 5 or pct_change < -5:
    """
    Get Bitcoin related news articles.
    """
    newsapi_parameters = {
        "q": "bitcoin",
        "category": "business",
        "language": "en",
        "apiKey": NEWSAPI_API_KEY,
    }

    # get json news data
    news = requests.get(NEWSAPI_ENDPOINT, params=newsapi_parameters)
    print(news.status_code)
    news.raise_for_status()
    news_data = news.json()

    # extract title, url and description
    articles = {}
    for article in news_data["articles"]:
        if article["source"]["name"] == "Bitcoin.com":
            articles[article["title"]] = (article["url"], article["description"])


    """
    Send sms.
    """
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body=f"{SYMBOL} {arrow_emoji}{pct_change}%\n"
                              f"{articles}",
                         from_='',
                         to=''
                     )
    print(message.sid)
