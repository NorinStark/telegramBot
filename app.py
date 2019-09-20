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

            transaction = dbcompanies.find({"setter": chat_id})
            for item in transaction:
                if item['company_name'] == None:
                    dbcompanies.update_one({"setter": chat_id},
                                           {"$set": {'company_name': message}})

                    updater.bot.send_message(chat_id=chat_id, text="Please select your Company:")
                    return "200"

                elif item["action"] == None:
                    dbcompanies.update_one({"setter": chat_id},
                                           {"$set": {'action': message}})

                    updater.bot.send_message(chat_id=chat_id, text="What do you want to do?")
                    return "200"

                elif item["package_amount"] == None:
                    dbcompanies.update_one({"setter": chat_id},
                                           {"$set": {'package_amount': message}})

                    updater.bot.send_message(chat_id=chat_id, text="How many packages in total?")
                    return "200"

                elif item["total_amount"] == None:
                    dbcompanies.update_one({"setter": chat_id},
                                           {"$set": {'total_amount': message}})

                    updater.bot.send_message(chat_id=chat_id, text="How much in total?")
                    return "200"

                elif item["upload_file"] == None:
                    dbcompanies.update_one({"setter": chat_id},
                                           {"$set": {'upload_file': message}})

                    updater.bot.send_message(chat_id=chat_id, text="Would you like to upload invoice?")

            files = {
                "setter_id": chat_id,
                "company_name": None,
                "action": None,
                "package_amount": None,
                "total_amount": None,
                "upload_file": None
            }

            data = dbcompanies.insert_one(files)

        except:
            True

        if message == '/start':
            updater.bot.send_message(chat_id=chat_id, text="Starting message here")

        elif message[8:] == '/company' or message[:11] == '/setcompany':
            try:
                if message[:8] == '/company':
                    name = data['message']['text'][8:]
                elif message[:11] == '/setcompany':
                    name = data['message']['text'][11:]

                CompanyName = name
                if CompanyName == '':
                    allcompanies = [
                        [KeyboardButton(text="/company BlocX"), KeyboardButton(text="/company Nham24"),
                         KeyboardButton(text="/company Joonaak"), KeyboardButton(text="/company Sousdey")]]

                    myreply = ReplyKeyboardMarkup(allcompanies, one_time_keyboard=True)
                    updater.bot.send_message(chat_id=chat_id, text="Please Select your Company:", reply_markup=myreply)

            except Exception as e:
                print(e)


    except Exception as e:
        print(e)

    return "200"

if __name__ == "__main__":
    app.run(port=80, debug=True)