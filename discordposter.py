#!/usr/local/bin/python3
import requests
import time

POST_URL = "https://discordapp.com/api/webhooks/666187507876233231/7bzJQ66O4T8GeGzip735FgEAacTgdLIqG2FJjZ-4OSjR7cAeMXlu1rpzTdidw1Y9VBmQ"
CITIES = [5110629, 5907166]

class post_it():
    def timeit(loop_time):
        start_time = time.time()
        while time.time() < (start_time + loop_time):
            time.sleep(loop_time)
            
    def bitcoin(post_url):
        bitcoins = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json").json()
        bitcoin_price = bitcoins['bpi']['USD']['rate']
        payload = {"content": "Bitcoin price: " + bitcoin_price}
        requests.post(post_url, data=payload)

    def weather(post_url, city):
        url = "http://api.openweathermap.org/data/2.5/forecast?id={}&APPID=34c57a50fddd3ed0f8a1b9e815acbab8".format(city)
        weather = requests.get(url).json()
        weather_temp = weather['list'][0]['main']['temp']
        weather_humidity = weather['list'][0]['main']['humidity']
        weather_sky= weather['list'][0]['weather'][0]['description']
        weather_date = weather['list'][0]['dt_txt']
        weather_city = weather['city']['name']
        real_temp = ((weather_temp - 273.15)*1.8)+32
        payload = {"content": "\nThe forcast for " + weather_date + " is as follows:\
        	   \n    _Temperature_: " + str(real_temp) + "\n    _Humidity_: " + str(weather_humidity) + "\
                   \n    _Clearness_: " + weather_sky + "\n    _City_: " + weather_city} 
        requests.post(post_url, data=payload)  

    def postthis(post_url, cities):
        try:
            while True:
                for the_city in cities:
                    post_it.weather(post_url, the_city)
                post_it.bitcoin(post_url)
                post_it.timeit(600)
                
        except Exception as e:
            print("Failure!: ", e)

post_it.postthis(POST_URL, CITIES)
