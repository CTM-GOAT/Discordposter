#!/usr/local/bin/python3
'''
Maintainer: Wesley Dugan
This is a discord poster

If you would like to use this. You will need to feed it an openweathermap api url
   a discord/slack url
'''
import requests
def weather(wurl):
    '''function to get weather info'''
    weather_json = requests.get(wurl).json()
    weather_temp = weather_json['list'][0]['main']['temp']
    weather_humidity = weather_json['list'][0]['main']['humidity']
    weather_sky = weather_json['list'][0]['weather'][0]['description']
    weather_date = weather_json['list'][0]['dt_txt']
    weather_city = weather_json['city']['name']
    real_temp = ((weather_temp - 273.15)*1.8)+32
    payload = {"content": "\nThe forecast for " + weather_date + " is as follows:\
        \n    _Temperature_: " + str(real_temp) + "\
        \n    _Humidity_: " + str(weather_humidity) + "\
        \n    _Clearness_: " + weather_sky + "\n    _City_: " + weather_city}
    return payload
def poster(post_url, payload):
    '''Function to post payload to url'''
    requests.post(post_url, data=payload)
