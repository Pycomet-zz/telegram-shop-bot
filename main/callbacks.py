from config import *
from utils import *
from .store import *

def second_menu(msg):
    res = get_products2()


    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard_buttons = []
    for i in res:
        key = types.InlineKeyboardButton(text=f"{i}", callback_data="Get Product")
        keyboard_buttons.append(key)
        keyboard.add(key)

    return keyboard


# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """

    if call.data == "Listing One":

        bot.send_message(
            call.from_user.id,
            "Select your product category and price from the list below ",
            reply_markup=second_menu(call)
        )
        bot.delete_message(call.message.chat.id, call.message.message_id)

    else:
        pass

