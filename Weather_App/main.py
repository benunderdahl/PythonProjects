import requests
from twilio.rest import Client

SID = 'SKa487d906c39d8b9e86c23e2'
api_key = 'Cq1bkpzYRJk2LZ7bMvCgJF61'
base_url = 'https://api.openweathermap.org/data/2.5/forecast'
account_sid = 'ACfe1e9d3271f86885a3277af8cdb'
auth_token = '7c14a258ea5412515cd1e7df8a'
twilio_num = '+14155238886'

params = {
    "lat": 29.4252,
    "lon": -98.4946,
    "appid": '08a654b044bf03aa5c829a1',
    "cnt": 4
}

response = requests.get(url=base_url, params=params)
response.raise_for_status()
data = response.json()
list = data["list"]
will_rain = False


for item in list:
    condition_code = item["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today bring an umbrella",
        from_= f"whatsapp:{twilio_num}",
        to= f"whatsa"
    )
    print(message.status)


