from pip import main
import json
import bot_commands
import requests 
from config import key
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def get_weather(city, key):
    # try:
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric")
    data = r.json()
    # data = json.loads(r.text)
    # print(data)
    city = data['name']
    curent_weather = data['main']['temp']
    curent_wind = data['wind']['speed']
    curent_pressure = data['main']['pressure']
    print(f' погода в городе: {city}\n температура: {curent_weather} \n скорость ветра: {curent_wind} \n давление: {curent_pressure}')
    # except Exception as ex:
        # print(ex)
        # print('введите правильное название')


def get_city(city, key):
    city = input('введите город: ')
    get_weather(city, key)
#     # if w == {'cod': '404', 'message': 'city not found'}:
    #     city = input('введите правильное название')
    #     print(w)

# get_city()

# if __name__ == get_weather:
#     get_weather()
