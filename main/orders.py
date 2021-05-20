from config import *


@bot.message_handler(regexp="^🛍 Orders")
def startorders(msg):
    "Returns a list of orders assosciated with a user"

    bot.reply_to(msg, "No Orders Made Yet!")