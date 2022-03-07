from math import prod
from config import *
from utils.functions import *
from .store import *

function = DbFuntions()

def payment_menu(product_id:int):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(text="Buy Product", callback_data=f"buy-{product_id}")
    keyboard.add(a)
    return keyboard

# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """
    query = call.data.split('-')

    if query[0] == "category":

        products = function.get_subcategories(query=query[1])
        if products != []:
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard_buttons = []
            for i in products:
                key = types.InlineKeyboardButton(text=f"{i}", callback_data=f"subcategory-{i}")
                keyboard_buttons.append(key)
                keyboard.add(key)

        bot.send_message(
            call.from_user.id,
            f"Select Your Product From The {query[1].upper()} Sub-Category ..",
            reply_markup=keyboard
        )
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif query[0] == "subcategory":
        
        products = function.get_products_by_subcategory(query=query[1])
        if products != None:
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard_buttons = []
            for i in products:
                key = types.InlineKeyboardButton(text=f"{i.name} - {i.price} credits", callback_data=f"product-{i.id}")
                keyboard_buttons.append(key)
                keyboard.add(key)

        bot.send_message(
            call.from_user.id,
            f"Select Your Product From The {query[1].upper()} Category ..",
            reply_markup=keyboard
        )
        bot.delete_message(call.message.chat.id, call.message.message_id)


    elif query[0] == "product":

        product = function.get_product_by_id(id=int(query[1]))

        bot.send_message(
            call.from_user.id,
            f"""
    <b>ID</b>: {product.id}
    <b>Name</b>: {product.name} - {product.price} credits

{product.desc}
------
{product.url}
            """,
            reply_markup=payment_menu(product_id=product.id),
            parse_mode="html"
        )
        bot.delete_message(call.message.chat.id, call.message.message_id)


    elif query[0] == "buy":

        product = function.get_product_by_id(id=int(query[1]))
        user = get_user(call)
        usd_balance = update_balance(call)

        #  get specific order

        if usd_balance <= float(product.price):
            bot.send_message(
                call.from_user.id,
                "Insufficient Funds In Your Account",
            )
        else:
            bot.send_message(
                call.from_user.id,
                "Purchase Request Processing!",
            )

            function.delete_product(product.id)
            bot.send_message(
                ADMIN_ID,
                f"Product {product.id} Sold & Deleted From Store!"
            )

            # create order
            order = function.create_order(call.from_user.id, product)

            unit_value_btc = client.get_rate(user.address)

            #deduct from balance
            charge_value = order.price / unit_value_btc
            vendor = function.get_vendor(id=product.owner)

            res1, res2 = function.charge_user(user, charge_value, vendor.address)

            bot.send_message(
                ADMIN_ID,
                f"New Purchase Payout Txid -- {res1} and {res2}"
            )

            if res1 == "Failed" or res2 == "Failed":
                bot.send_message(
                    call.from_user.id,
                    "Please update your balance to make payouts. Error occurred due to insufficient amount in your wallet"
                )

            else:    
                bot.send_message(
                    call.from_user.id,
                    f"""
    <b>Product Id:</b> {product.id}
    <b>Name:</b> {product.name}
    ----------------
    <b>Category:</b> {product.category}
    <b>Description:</b> {product.desc}
    <b>Url:</b> {product.url}
                    
                    """,
                    parse_mode="html"
                )

        bot.delete_message(call.message.chat.id, call.message.message_id)



    else:
        pass

