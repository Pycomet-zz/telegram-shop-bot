import json

def get_orders(user_id):
    "Returns all orders attached to a specifici user"
    pass


def get_products1():
    "Pulls down al the store products"
    file = open('./products.json')
    data = json.load(file)
    return data['First Listing']



def get_products2():
    "product types & prices"
    file = open('./products.json')
    data = json.load(file)
    return data['Second Listing']  