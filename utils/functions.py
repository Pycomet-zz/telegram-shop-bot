import json
from models import User, session
from wallet import WalletApi

client = WalletApi()

def get_orders(id):
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


def get_user(msg):
    "Returns or creates a new user"
    id = msg.from_user.id
    
    user = session.query(User).filter_by(id=id).first()
    if user:
        return user
    else:
        mnemonic, address = client.create_wallet()
        user = User(id=id, balance="0", orders=0, address=address, mnemonic=mnemonic)
        session.add(user)
        session.commit()
        return user

def update_balance(msg):
    "Updates User Balance"
    user = get_user(msg)

    balance = client.get_balance(address = user.address)
    user.balance = str(balance)
    session.add(user)
    session.commit()
    return str(balance)


def get_received_msg(msg):
    "Delete This Message"

    message_id = msg.message_id
    chat = msg.chat
    return chat, message_id

def send_out_payment(user, amount, wallet):
    status = client.send_money(user, amount, wallet)
    return status
