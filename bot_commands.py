import data_provider as dp
from telegram import Update, message
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from config import key
import requests 


def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Привет,{update.effective_user.first_name}! Я бот показывающий погоду! Если интересно - вводи город! Нет - сорян!')

def time_command(update: Update, context: CallbackContext):
    # log(update, context)
    update.message.reply_text(f'Время {datetime.datetime.now().time()}')

def bye_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Пока {update.effective_user.first_name}')

def city_command(update: Update, context: CallbackContext):
    # msg = update.message.text
    # print(msg)
    update.message.reply_text (dp.get_weather(update, context))
    # print (f'Погода: {dp.get_weather()}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f' /hi\n/time\n/bye\n/help\n/city {update.effective_user.first_name}')

# city_command()