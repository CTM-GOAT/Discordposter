#!/usr/local/bin/python3
import requests

POST_URL = "https://discordapp.com/api/webhooks/666187507876233231/7bzJQ66O4T8GeGzip735FgEAacTgdLIqG2FJjZ-4OSjR7cAeMXlu1rpzTdidw1Y9VBmQ"

def bitcoin():
    bitcoins = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json").json()
    bitcoin_price = bitcoins['bpi']['USD']['rate']
    return bitcoin_price

def weather(post_url, bitcoin_price):
    url = "http://api.openweathermap.org/data/2.5/forecast?id=5819881&APPID=34c57a50fddd3ed0f8a1b9e815acbab8"
    weather = requests.get(url).json()
    weather_temp = weather['list'][1]['main']['temp']
    weather_humidity = weather['list'][1]['main']['humidity']
    weather_sky= weather['list'][1]['weather'][0]['description']
    weather_date = weather['list'][1]['dt_txt']
    weather_city = weather['city']['name']
    real_temp = (((weather_temp - 273.15)*9)/5)+32

    payload = {"content": "The forcast for " + weather_date + " is as follows:\
               \nTemperature: " + str(real_temp) + "\nHumidity: " + str(weather_humidity) + "\
               \nClearness: " + weather_sky + "\nCity: " + weather_city + "\n\nOn a side note Bitcoin is at: " + bitcoin_price + ":moneybag:"}
    requests.post(post_url, data=payload)    


weather(POST_URL, bitcoin())
