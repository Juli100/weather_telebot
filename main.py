from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
# from bot_commands import hi_command, time_command, city_command, help_command, bye_command
from bot_commands import *

updater = Updater('5285083920:AAFaNBuQErlTIOLPYJnfMyCGAWGK169vRzA')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('city', city_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('bye', bye_command))

print('sever start')
updater.start_polling()
updater.idle()
