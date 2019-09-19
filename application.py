import os
from flask import Flask, request
import telebot

TOKEN = '869700453:AAFYPaaF_zCeIocVcdYiDNCLp4PkcpJi7t4'
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Ok", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://norin-telegram-bot.herokuapp.com/' + TOKEN)
    bot.send_message(chat_id='', text='Please come to PickUp the Package!')
    return "Ok", 200

bot.polling()

if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 5000)))