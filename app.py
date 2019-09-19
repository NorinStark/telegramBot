from flask import Flask, request, jsonify, Response
import requests
import json
import datetime
import pymongo
from bson.json_util import dumps
from flask_api import status
import re
import telegram
from telegram.ext import Updater
from telegram import keyboardbutton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import time


from telegram_bot import TelegramBot
from config import TELEGRAM_INIT_WEBHOOK_URL, TOKEN

app = Flask(__name__)
TelegramBot.init_webhook(TELEGRAM_INIT_WEBHOOK_URL)

def parse_message(message):
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']

    pattern = r'/[a-zA-Z]{2,4}'
    ticker = re.findall(pattern, txt)

    if ticker:
        symbol = ticker[0][1:].upper()
    else:
        symbol = ''

    return chat_id, symbol

def send_message(chat_id, text='Hello there!'):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}

    res = requests.post(url, json=payload)

@app.route("/", methods=['POST', 'GET'])
def webhook():

    if request.methods == 'POST':
        message = request.get_json()
        chat_id, symbol = parse_message(message)

        if not symbol:
            send_message(chat_id, 'Wrong Data')
            return Response('ok', status=200)

    else:
        return '<h1>Norin_Stark Bot</h1>'



if __name__ == "__main__":
    app.run(debug=True)