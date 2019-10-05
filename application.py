import logging
import requests
import json
from telegram import *
#from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import *

from pymongo import MongoClient
from pymongo.errors import WriteError
from pymongo.errors import WriteConcernError
from datetime import datetime
import time


mongolab_uri = "mongodb+srv://Sixsixone5:42577400Vj@chatbot-general-p2ykh.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(mongolab_uri,
                     connectTimeoutMS=10000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)

db = client.get_default_database()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)
COMPANY, ACTION, PACKAGES, AMOUNT, PHOTO = range(5)

genre=""
def start(update, context):
    reply_keyboard = [['BlocX', 'Joonak', 'Nham24', 'Cambodia Express']]

    update.message.reply_text(
        'Welcome to SOUSDEY CAMBODIA Bot!'
        'Send /cancel to stop talking to the bot.\n\n'
        'What is your company?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return COMPANY

def company(update, context):
    reply_keyboard = [['PICK UP', 'RETURN', 'PAYMENT']]

    user = update.message.from_user
    logger.info("Company of %s: %s", user.first_name, update.message.text)
    genre=update.message.text
    update.message.reply_text(
        'What do you want to do?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return ACTION

def action(update, context):
    user = update.message.from_user
    logger.info("Goal of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        'How many Packages in total?',
        reply_markup=ReplyKeyboardRemove())

    return PACKAGES

def package(update, context):
    user = update.message.from_user
    logger.info("%s have %s packages in total", user.first_name, update.message.text)
    update.message.reply_text(
        'What is the total amount?',
        reply_markup=ReplyKeyboardRemove())

    return AMOUNT

def amount(update, context):
    user = update.message.from_user
    logger.info("Amount of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        'Would you like to send the invoice?'
        'or send /skip if you don\'t want to.',
        reply_markup=ReplyKeyboardRemove())

    return PHOTO

def photo(update, context):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    logger.info("photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text(
        'Thank you! Information is saved!',
        reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def skip_photo(update, context):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text(
        'Thank you! Information is saved!',
        reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye Bye! Have a great day!',
        reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def error(update, context):
    # Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def handlePhoto(update, context):
    fileImg1 = context.bot.getFile(update.message.photo[-1].file_id)['file_path']
    # fileImg = clientF.upload(external_url=fileImg1) A9pFKleJFTD2XjjiccHxBz
    urlF = "https://www.filestackapi.com/api/store/S3?key=A9pFKleJFTD2XjjiccHxBz"
    r = requests.post(urlF, data={'url': fileImg1})
    print(r)
    fileImg=json.loads(r.text)["url"]
    print(fileImg)
    currentUser=update.message.from_user
    now = datetime.now()
    s2 = now.strftime("%d/%m/%Y")