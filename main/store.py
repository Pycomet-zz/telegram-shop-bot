from config import *
from utils import get_products1
import json

def menu(msg):
    res = get_products1()

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard_buttons = []
    for i in res:
        key = types.InlineKeyboardButton(text=f"{i}", callback_data="Listing One")
        keyboard_buttons.append(key)
        keyboard.add(key)

    return keyboard



@bot.message_handler(regexp="^🛒 Store")
def start_store(msg):
    "Brings up the store menu with information for purchase"

    user_id = msg.from_user.id 

    bot.reply_to(msg, "Welcome To The ShopBot Store 🛒", reply_markup=menu(msg))