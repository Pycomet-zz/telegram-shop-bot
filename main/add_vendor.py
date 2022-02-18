from config import *
from utils.functions import DbFuntions

@bot.message_handler(commands=['newvendor'])
def verify(msg):
    """
    Verifying an vendor account
    """
    
    if int(msg.from_user.id) != int(ADMIN_ID):
        bot.reply_to(
            msg,
            "You are not authorized to use this command."
        )
        
    else:

        question = bot.send_message(
            msg.from_user.id,
            "Paste in the User's ID?"
        )
        # question = question.wait()
        bot.register_next_step_handler(question, add_vendor)
        


def add_vendor(msg):
    """
    Create new vendor
    """

    vendor = DbFuntions().create_vendor(
        user_id = int(msg.text)
    )

    if vendor != None:
        bot.send_message(
            msg.from_user.id,
            "<b>New Vendor {vendor.id} Created!</b>",
            parse_mode="HTML"
        )
    else:
        bot.send_message(
            msg.from_user.id,
            "Invalid Vendor ID"
        )