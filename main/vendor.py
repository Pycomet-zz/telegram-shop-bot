from math import prod
from config import *
from utils.functions import DbFuntions

def vendor_menu(msg):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    a = types.KeyboardButton("Add New Product 🟢")
    b = types.KeyboardButton("View All Products 🟡")
    c = types.KeyboardButton("Delete Product 🔴")
    d = types.KeyboardButton("Calculate Total Sales 💹")

    keyboard.add(a,b,c,d)
    return keyboard

function = DbFuntions()

@bot.message_handler(commands=['vendor'])
def vendor(msg):
    "This Opens the Vendor Service"
    vendor = function.get_vendor(id=msg.from_user.id)
    if vendor != None:
        bot.reply_to(
            msg,
            f"Welcome to your Vendor Panel {msg.from_user.first_name}",
            reply_markup=vendor_menu(msg)
        )
    elif msg.from_user.id == ADMIN_ID:

        bot.reply_to(
            msg,
            f"Welcome to your Vendor Panel {msg.from_user.first_name}",
            reply_markup=vendor_menu(msg)
        )
    else:
        bot.reply_to(
            msg,
            f"{vendor} {ADMIN_ID} You are not a vendor, contact support!"
        )




@bot.message_handler(regexp=['^View All Products 🟡'])
def view_products(msg):
    "This Returns All the User's Products"

    products = function.get_user_products(user_id=msg.from_user.id)

    if products != None:
        
        for product in products:
            bot.send_message(
                msg.from_user.id,
                f"""
<b>Product Id:</b> {product.id}
<b>Name:</b> {product.name}
----------------
<b>Category:</b> {product.category}
<b>Description:</b> {product.desc}
<b>Cost:</b> ${product.price}
<b>Url:</b> {product.url}

<b>Sales: {len(product.orders)}</b>
                
                """,
                parse_mode="html"
            )

    else:

        bot.send_message(
            msg.from_user.id,
            "You have no product in your inventory."
        )




@bot.message_handler(regexp=['^Delete Product 🔴"'])
def delete_product(msg):


    question = bot.send_message(
        msg.from_user.id,
        "What is the ID of the Product you wish to deleted .."
    )
    # question = question.wait()
    bot.register_next_step_handler(question, remove_product)


def remove_product(msg):
    product = function.get_product_by_id(
        id=int(msg.text)
    )
    if product is not None:

        if product.owner == msg.from_user.id:
            function.delete_product(id=product.id)

            bot.send_message(
                msg.from_user.id,
                "Product Deleted Successfully!"
            )
        else:

            bot.send_message(
                msg.from_user.id,
                "You are not the owner of the product so you can not delete it!"
            )
    
    else:

        bot.send_message(
            msg.from_user.id,
            "Product Not Found!"
        )
