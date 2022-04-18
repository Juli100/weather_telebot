# import bot_commands
import json
import requests 
from config import key
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def get_weather(update: Update, context: CallbackContext):
    # try:
    city = update.message.text.split()[1]
    # print(city)
    # city = input('введите город: ')
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric")
    if int(r.status_code/100) == 4:
        return 'введите правильное название'
    else:

        data = r.json()
        print(r.status_code)
    # print(data)
        town = data['name']
        curent_weather = data['main']['temp']
        curent_wind = data['wind']['speed']
        curent_pressure = (float(data['main']['pressure']) * 0.75)
        return (f' погода в городе: {town}\n температура: {curent_weather} \n скорость ветра: {curent_wind} \n давление: {curent_pressure}')







# def get_city(update: Update, context: CallbackContext):
    # city = input('введите город: ')
#     gorog = update.message.text
#     get_weather(gorog)
# #     # if w == {'cod': '404', 'message': 'city not found'}:
    #     city = input('введите правильное название')
    #     print(w)

# get_weather()

# if __name__ == "__main__":
#     get_weather()
