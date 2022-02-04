from config import *


@bot.message_handler(regexp="^📞 Support")
def startorders(msg):
    "Returns a helper message"

    bot.reply_to(msg, "We Are Here To Help Everyday! EveryTime.")

    question = bot.send_message(
        msg.from_user.id,
        "What can we help you do today? Please explain it to us here ...",
    )
    
    bot.register_next_step_handler(question, send_complaint)



def send_complaint(msg):
    "Sends Complaint Message To Admin"

    # get Admin ID

    