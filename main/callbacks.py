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

def payment_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text="Buy Product", callback_data="Buy")
    b = types.InlineKeyboardButton(text="Go Back", callback_data="Listing One")
    keyboard.add(a, b)
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

    elif call.data == "Get Product":

        bot.send_message(
            call.from_user.id,
            """
    ID: 12890
    Name: Debit-online+email - 2200$

s a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
            """,
            reply_markup=payment_menu()
        )
        bot.delete_message(call.message.chat.id, call.message.message_id)


    elif call.data == "Buy":

        user = get_user(call)
        balance = update_balance(call)

        #  get specific order

        if float(balance) != 0:
            bot.send_message(
                call.from_user.id,
                "Insufficient Funds In Your Account",
            )
        else:
            bot.send_message(
                call.from_user.id,
                "Purchase Request Successfull",
            )

        bot.delete_message(call.message.chat.id, call.message.message_id)



    else:
        pass

