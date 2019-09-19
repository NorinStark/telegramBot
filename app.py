from flask import Flask, request, jsonify
import requests
import json
import datetime
import pymongo
import telegram
from telegram.ext import Updater
from telegram import keyboardbutton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import time

from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL

app = Flask(__name__)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

bot = telegram.Bot(token='869700453:AAFYPaaF_zCeIocVcdYiDNCLp4PkcpJi7t4')

token = '869700453:AAFYPaaF_zCeIocVcdYiDNCLp4PkcpJi7t4'

@app.route("/", methods=["GET"])
def hello():
    print('Hello World!')

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print(data)

    bot = TelegramBot()
    bot.parse_webhook_data(data)
    success = bot.action()
    return jsonify(sucess=success)



if __name__ == "__main__":
    app.run(port=80, debug=True)