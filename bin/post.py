#!/usr/local/bin/python3
'''Used to feed discordposter information (more modular)'''
from time import sleep
from discordposter import weather, poster
WURL = "http://api.openweathermap.org/data/2.5/forecast?id=\
{}&APPID=34c57a50fddd3ed0f8a1b9e815acbab8"
PURL = "https://discordapp.com/api/webhooks/669240324832624650/\
OyUdVPItBzmliArPnHmN8bxXiw__YlQKPE0rRdLUwM2UqqN_kzKdUH7GXvZ7R9B7JSpj"
CITIES = [5110629, 5907166, 1701667]

while True:
    for city in CITIES:
        weather_city = weather(WURL.format(city))
        poster(PURL, weather_city)
    sleep(10800)
