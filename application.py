from flask import Flask, request
import requests
import json
import datetime
import pymongo
import telegram
from telegram.ext import Updater
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
import time
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb+srv://Sixsixone5:42577400Vj@chatbot-general-p2ykh.mongodb.net/test?retryWrites=true&w=majority")

messages = myclient["delivery"]

bot = telegram.Bot(token='869700453:AAFYPaaF_zCeIocVcdYiDNCLp4PkcpJi7t4')

token = '869700453:AAFYPaaF_zCeIocVcdYiDNCLp4PkcpJi7t4'


@app.route("/", methods=['GET'])
def hello():
    print('get here')


@app.route("/", methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    chat_id = data['message']['chat']['id']
    updater = Updater(token='869700453:AAFYPaaF_zCeIocVcdYiDNCLp4PkcpJi7t4')

    dbcompanies = messages["set_company"]

    try:
        message = data['message']['text']
        try:
            files = {
                "setter_id": chat_id,
                "company_name": "Null",
                "action": "Null",
                "package_amount": "Null",
                "total_amount": "Null",
                "upload_file": "Null"
            }

            data = dbcompanies.insert_one(files)

        except Exception as e:
            print(e)

        if message == '/start':
            updater.bot.send_message(chat_id=chat_id, text="Starting message here")


    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(port=80, debug=True)