from config import *

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

    # IF USER NEW, CREATE WALLET INFO

    bot.reply_to(
        msg,
        """
⚠️ Please avoid sharing any information in the section of this application with any third-party for safety.

Select Action From The Buttons You See Below 
        """,
        reply_markup=menu(msg)
    )




@bot.message_handler(regexp="^⬇️ Deposit")
def deposit(msg):
    "Returns wallet address for user to deposit to their account"

    # FETCH THE USER'S WALLET ADDRESS

    bot.reply_to(
        msg,
        "Fetching your wallet address ..."
    )





@bot.message_handler(regexp="^⬆️ Withdraw")
def withdraw(msg):
    "Retries User Address And Make Payment"

    # Ask how much they wish to withdraw

    # Compare price with balance

    # If balance is higher
        # Send out payment

    # If balance is lower
        # Returns bold message (insufficient funds)

    