import os
import time
from flask import Flask, request
import telebot
from telebot import types
from flask_pymongo import PyMongo
from dotenv import load_dotenv
load_dotenv()


# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )


TOKEN = os.getenv('TOKEN')

DEBUG = False


DATABASE_URL = os.getenv("DATABASE")

ADMIN_ID = os.getenv("ADMIN_ID")

ADMIN_WALLET = os.getenv("ADMIN_WALLET")

SERVER_URL = os.getenv("SERVER_URL")

FORGING_BLOCK_TOKEN = os.getenv("FORGING_BLOCK_TOKEN")

MAIL = os.getenv("MAIL")
PASS = os.getenv("PASS")

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
server.config["MONGO_URI"] = os.getenv('MONGO_URL')

mongo = PyMongo(server)

db = mongo.db

import importdir
importdir.do("utils", globals())