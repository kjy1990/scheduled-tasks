import requests
from twilio.rest import Client
import os

account_sid =  os.environ.get(TWILIO_SID)
auth_token = os.environ.get(TWILIO_TOKEN)
PARAM= {
    "lat":1.308520,
    "lon":103.910029,
    "appid":"e92762631373517c9f92962978a87bc8",
    "cnt":4
}


connection=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=PARAM)
connection.raise_for_status()
data=connection.json()["list"]

for _ in range(len(data)):
    weather_codes=data[_]["weather"][0]["id"]
    if weather_codes <700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Testing, testing, testing. It'll rain",
            from_='whatsapp:+14155238886',
            to="whatsapp:+6598163596",
        )
        print(message.status)
