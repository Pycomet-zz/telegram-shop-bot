import os
import telegram
import time
from flask import Flask, request
import telebot
from telebot import types
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

FORGING_BLOCK_TOKEN = os.getenv("FORGING_BLOCK_TOKEN")

MAIL = os.getenv("MAIL")
PASS = os.getenv("PASS")

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

import importdir
importdir.do("utils", globals())