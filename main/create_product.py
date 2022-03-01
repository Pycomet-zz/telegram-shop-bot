from pydoc import text
from unicodedata import category

from sqlalchemy import func
from config import *
from utils.functions import DbFuntions


function = DbFuntions()

@bot.message_handler(regexp='^Add New Product 🟢')
def product_create(msg):
    "Creates A New Product For The User"
    # import pdb; pdb.set_trace()

    vendor = function.get_vendor(msg.from_user.id)

    if vendor == None:
        bot.reply_to(
            msg,
            "You are not authorized vendor, contact support if you wish to sell with this service."
        )

    elif int(msg.from_user.id) == int(ADMIN_ID):

        question = bot.send_message(
            msg.from_user.id,
            "Let's get started creating a new product. What is the Product's Name ?"
        )
        # question = question.wait()
        bot.register_next_step_handler(question, create_product)      
        
    else:

        question = bot.send_message(
            msg.from_user.id,
            "Let's get started creating a new product. What is the Product's Name ?"
        )
        # question = question.wait()
        bot.register_next_step_handler(question, create_product)
        



def create_product(msg):
    "Create A New Product"
    name = msg.text

    product = function.create_product(
        user_id=msg.from_user.id,
        name=name
    )

    question = bot.send_message(
        msg.from_user.id,
        "Paste in the category name as list on the menu without the emoji .."
    )
    # question = question.wait()
    bot.register_next_step_handler(question, add_category)



def add_category(msg):
    "Add Category"
    category = msg.text.lower()

    categories = function.get_categories()
    for each in categories:
        if each.lower() == category:

            status = function.add_category(text=category)

            if status == False:

                bot.reply_to(
                    msg,
                    "Wrong Category! Start over!"
                )
            
            else:
                question = bot.send_message(
                    msg.from_user.id,
                    "Paste in the sub-category name for this product without the emoji .."
                )
                # question = question.wait()
                bot.register_next_step_handler(question, add_subcategory)


def add_subcategory(msg):
    "Adding A Sub Category"
    category = msg.text.lower()

    categories = function.get_all_subcategories()
    for each in categories:
        if each.lower() == category:

            status = function.add_subcategory(text=category)

            if status == False:

                bot.reply_to(
                    msg,
                    "Wrong Sub Category! Start over!"
                )
            
            else:
                question = bot.send_message(
                    msg.from_user.id,
                    "Please provide a brief description of your product .."
                )
                # question = question.wait()
                bot.register_next_step_handler(question, add_desc)


def add_desc(msg):
    "Add Description"
    desc = msg.text

    res = function.add_desc(desc=desc)
    if res == False:

        bot.reply_to(
            msg,
            "Wrong Input! Start over!"
        )
    
    else:
        question = bot.send_message(
            msg.from_user.id,
            "Please place a USD value cost for you product. Just numbers (No commas or symbols) .."
        )
        # question = question.wait()
        bot.register_next_step_handler(question, add_price)


def add_price(msg):
    "Add Price"
    price = int(msg.text)


    res = function.add_price(price=price)
    if res == False:

        bot.reply_to(
            msg,
            "Wrong Input! Start over!"
        )
    
    else:
        question = bot.send_message(
            msg.from_user.id,
            "Please paste a url linking to any visual or extensive resource for this product (type 'None' if none available) .."
        )
        # question = question.wait()
        bot.register_next_step_handler(question, add_url)



def add_url(msg):
    "Add url"
    url = msg.text

    res, product_id = function.add_url(url=url)
    if res == False:

        bot.reply_to(
            msg,
            "Wrong Input! Start over!"
        )
    
    else:
        
        bot.send_message(
            msg.from_user.id,
            f"New Product Created Successfully {product_id}"
        )
