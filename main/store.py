from config import *

@bot.message_handler(regexp="^🛒 Store")
def start_store(msg):
    "Brings up the store menu with information for purchase"

    user_id = msg.from_user.id 

    