from config import *
from utils.functions import DbFuntions

@bot.message_handler(commands=['broadcast'])
def blast(msg):
    "Send Broadcast To All Vendors"

    if msg.from_user.id == int(ADMIN_ID):
        bot.reply_to(
            msg,
            "You are not authorized to use this command."
        )
        
    else:
        question = bot.send_message(
            msg.from_user.id,
            "Please Paste In The Broadcast Message For All Vendors .."
        )
        # question = question.wait()
        bot.register_next_step_handler(question, send_broadcast)
        


def send_broadcast(msg):
    "Send Blast"

    vendors = DbFuntions().get_all_vendors()

    for vendor in vendors:

        bot.send_message(
            vendor.id,
            msg.text
        )

    bot.reply_to(
        msg,
        "Done😃"
    )