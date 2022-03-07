from unicodedata import name
from config import *
from utils.functions import DbFuntions
import json

def menu(msg):
    res = DbFuntions().get_categories()

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard_buttons = []
    for i in res:
        key = types.InlineKeyboardButton(text=f"🏦  {i}", callback_data=f"category-{i}")
        keyboard_buttons.append(key)
        keyboard.add(key)

    return keyboard



@bot.message_handler(regexp="^🛒 Store")
def start_store(msg):
    "Brings up the store menu with information for purchase"

    user_id = msg.from_user.id 

    bot.reply_to(
        msg,
        """
        Welcome To The ShopBot Store 🛒 
        
note: <b>1 credit is equal to $1</b>""",
        reply_markup=menu(msg),
        parse_mode="html"
    )