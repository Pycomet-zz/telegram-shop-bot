import os
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

DEBUG = True

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)