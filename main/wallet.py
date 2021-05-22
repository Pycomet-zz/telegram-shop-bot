from requests.api import request
from config import *
from utils import *

def menu(msg):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    a = types.KeyboardButton("⬇️ Deposit")
    b = types.KeyboardButton("⬆️ Withdraw")
    c = types.KeyboardButton("My Balance 💰")
    keyboard.add(a, b, c)
    return keyboard


@bot.message_handler(regexp="^💳 Wallet")
def startwallet(msg):
    "Starts the wallet section"

    user = get_user(msg)

    bot.reply_to(
        msg,
        """
⚠️ Please avoid sharing any information in the section of this application with any third-party for safety.

Select Action From The Buttons You See Below 
        """,
        reply_markup=menu(msg)
    )




@bot.message_handler(regexp="^My Balance 💰")
def balance(msg):
    "Returns user's balance"

    user = get_user(msg)

    bot.reply_to(
        msg,
        f"Your Bitcoin Balance - <b>{user.balance} BTC </b>",
        parse_mode=telegram.ParseMode.HTML,
    )

@bot.message_handler(regexp="^⬇️ Deposit")
def deposit(msg):
    "Returns user's address for deposit to wallet"

    user = get_user(msg)

    bot.reply_to(
        msg,
        f"⚠️ Copy Paste The Wallet Address Below To Deposit Into You Account's Wallet.",
    )

    bot.send_message(
        user.id,
        f"<b>{user.address}</b>",
        parse_mode=telegram.ParseMode.HTML,       
    )




@bot.message_handler(regexp="^⬆️ Withdraw")
def withdraw(msg):
    "Retries User Address And Make Payment"

    # Ask how much they wish to withdraw
    question = bot.reply_to(
        msg,
        "How much of your available bitcoin do you wish to withdraw?",
    )
    bot.register_next_step_handler(question, process_withdrawal)


def process_withdrawal(msg):

    # Compare price with balance
    global request_price
    request_price = msg.text
    user = get_user(msg)

    if float(user.balance) >= float(request_price):

        bot.send_message(
            user.id,
            "<b>Withdrawal Request Accepted</b>",
            parse_mode=telegram.ParseMode.HTML,     
        )

        # Make payment
        question = bot.send_message(
            user.id,
            "Paste the wallet address you wish to be paid into (⚠️ must be a bitcoin wallet address)"
        )
        bot.register_next_step_handler(question, make_payment)

    else:

        bot.send_message(
            user.id,
            "<b>Withdrawal Request Denied! Insufficient Funds On Your Account</b>",
            parse_mode=telegram.ParseMode.HTML,     
        )



def make_payment(msg):
    "Make payment out to user"
    wallet = msg.text
    amount = request_price
    user = get_user(msg)

    result = send_out_payment(user, amount, wallet)

    if result != "Failed":

        bot.send_message(
            user.id,
            f"<b>Bitcoin Sent Out Successfully, Here Is The Transaction ID - {result}</b>",
            parse_mode=telegram.ParseMode.HTML, 
        )

    else:

        bot.send_message(
            user.id,
            f"<b>Bitcoin Sent Out Failed! Try Again With A Lesser Amount",
            parse_mode=telegram.ParseMode.HTML, 
        )


