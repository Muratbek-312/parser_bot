import telebot
import requests
from bs4 import BeautifulSoup
from decouple import config
from keyboards.inline import inline_keyboard as in_key

bot = telebot.TeleBot(config("TOKEN"))


@bot.message_handler(commands=['start', ])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Hello', reply_markup=in_key)

bot.polling(none_stop=True)