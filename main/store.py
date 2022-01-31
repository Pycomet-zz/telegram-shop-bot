from unicodedata import name
from config import *
from utils import DbFuntions
import json

def menu(msg):
    res = DbFuntions().get_categories()

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard_buttons = []
    for i in res:
        key = types.InlineKeyboardButton(text=f"🏦  {i[name]}", callback_data="Categories")
        keyboard_buttons.append(key)
        keyboard.add(key)

    return keyboard



@bot.message_handler(regexp="^🛒 Store")
def start_store(msg):
    "Brings up the store menu with information for purchase"

    user_id = msg.from_user.id 

    bot.reply_to(msg, "Welcome To The ShopBot Store 🛒", reply_markup=menu(msg))