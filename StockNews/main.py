import requests
import os
from twilio.rest import Client



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": os.getenv("STOCK_API_KEY")
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday = data_list[0]
day_before_yesterday = data_list[1]

difference = abs(float(yesterday["4. close"]) - float(day_before_yesterday["4. close"]))
diff_percent = (difference / float(yesterday["4. close"])) * 100
diff_percent = 5


if diff_percent > 1:
    print("get the news")
    news_params = {
        "apiKey": os.getenv("NEWS_API_KEY"),
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    news_articles = news_data[:3]
    print(news_articles)
    head_brief = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_articles]
    client = Client(os.getenv("twilio_sid"), os.getenv("twilio_auth"))
    for article in head_brief:
        message = client.messages.create(body=article, from_=f"whatsapp:{os.getenv("whatsapp_num")}", to=f"whatsapp:{os.getenv("my_num")}")
        print(message.sid)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

