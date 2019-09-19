from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import time
import schedule

def bot_senttext(message):
    token = '869700453:AAFYPaaF_zCeIocVcdYiDNCLp4PkcpJi7t4'

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('869700453:AAFYPaaF_zCeIocVcdYiDNCLp4PkcpJi7t4')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('hey',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()