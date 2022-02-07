from config import *
from utils.functions import DbFuntions
from utils.models import Order


@bot.message_handler(regexp="^🛍 Orders")
def startorders(msg):
    "Returns a list of orders assosciated with a user"

    orders_obj = DbFuntions().get_user_orders(msg.from_user.id)
    orders = [i for i in orders_obj]

    if orders != []:
        for order in orders:
            bot.send_message(
                msg.from_user.id,
                f"""
    <b>Order Details</b>
    Product Id - {order.product_id}
    Product Cost - {order.cost}
                """,
                parse_mode="html"
            )

    else:

        bot.reply_to(msg, "No Orders Made Yet!")