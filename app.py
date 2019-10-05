from flask import Flask, request
import logging
import requests
import json
from telegram import *
from telegram.ext import *
from pymongo import MongoClient
from pymongo.errors import WriteError
from pymongo.errors import WriteConcernError
from datetime import datetime
import time


app = Flask(__name__)

myclient = MongoClient("mongodb+srv://Sixsixone5:42577400Vj@chatbot-general-p2ykh.mongodb.net/test?retryWrites=true&w=majority")

messages = myclient.get_default_database()

#Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

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
                    return "200"

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

        elif message[7:] == '/action' or message[:10] == '/setaction':
            try:
                if message[7:] == '/action':
                    action = data['message']['text'][7:]
                elif message[:10] == '/setaction':
                    action = data['message']['text'][:10]

                option = action
                if option == '':
                    alloptions = [KeyboardButton(text="/Return"), KeyboardButton(text="/Payment")]

                    myreply = ReplyKeyboardMarkup(alloptions, one_time_keyboard=True)
                    updater.bot.send_message(chat_id=chat_id, text="What do you want to do?", reply_markup=myreply)

            except Exception as e:
                print(e)

        elif message[9:] == '/packages':
            try:
                if message[9:] == '/packages':
                    package = data['message']['text'][9:]

                total_packages = package
                if total_packages == '':
                    updater.bot.send_message(chat_id=chat_id, text="How many packages in total?")

            except Exception as e:
                print(e)

        elif message[7:] == '/amount':
            try:
                if message[7:] == '/amount':
                    amount = data['message']['text'][7:]

                total_amount = amount
                if total_amount == '':
                    updater.bot.send_message(chat_id=chat_id, text="How much is total amount?")
            except Exception as e:
                print(e)

    except:
        try:
            message = data['message']['photo']
            dbcol = messages['set_company']
            dbinputs = messages['inputs']

        if file_id = data['message']['photo'][0][]:


        except Exception as e:
            print(e)

    return "200"



if __name__ == "__main__":
    app.run(port=80, debug=True)