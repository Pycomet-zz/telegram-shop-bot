from ast import Or
import json
from re import U
from unicodedata import category
from xmlrpc.client import Boolean

from flask import session
from config import *
from utils.models import *
from wallet import WalletApi

client = WalletApi()


class DbFuntions(object):

    def __init__(self) -> None:
        pass

    def get_categories(self):
        "Pulls down al the store categories"
        file = open('./products.json')
        data = json.load(file)
        res = data['Categories']
        return res


    def get_user_products(cls, user_id:int) -> Product | None:
        "Fetch product by a specific ID"
        products = session.query(Product).filter_by(owner=user_id)
        return products

    def get_products_by_category(cls, query:str) -> Product | None:
        "Fetch Products by category"
        products = session.query(Product).filter_by(category=query)
        return products

    def get_product_by_id(cls, id:int) -> Product | None:
        product = session.query(Product).filter_by(id=id).first()
        return product


    def create_vendor(cls, user_id:int) -> Vendor:
        "Create A New Vendor To The dateabase"
        vendor = session.query(Vendor).filter_by(id=user_id).first()

        user = get_user(user_id)

        if vendor is None:

            vendor = Vendor(
                id=user_id,
                address=user.address,
                mnemonic=user.mnemonic
            )
            session.add(vendor)
            session.commit()

    def get_all_vendors(cls) -> list:
        "Fetch All Vendors"
        vendors = session.query(Vendor)
        return vendors

    def get_user_orders(cls, user_id:int) -> list:
        orders = session.query(Order).filter_by(id=user_id)
        return orders

    def get_vendor(cls, id:str) -> Vendor | None:
        vendor = session.query(Vendor).filter_by(id=id).first()
        return vendor


    def create_product(self, user_id, name):
        "Insert Product To Database"
        index = session.query(Product).count() + 1

        self.product = Product(
            id=index,
            owner=user_id,
            name=name
        )
        session.add(self.product)
        session.commit()

    def create_order(self, user_id:int, product:Product) -> Order:
        order = Order(
            id=user_id,
            product=product,
            cost=str(product.price),
            product_id=product.id
        )
        session.add(order)
        session.commit()
        return order

    def add_category(self, text:str) -> Boolean:
        "Add Category Of Product"
        categories = self.get_categories()

        if text in categories:
            self.product.category = text
            session.add(self.product)
            return True
        else:
            return False

    def add_desc(self, desc:str) -> Boolean:
        "Add Description"
        try:
            self.product.desc = desc
            session.add(self.product)
            return True
        except:
            return False

    def add_price(self, price:int) -> Boolean:
        "Add Price"
        try:
            self.product.price = price
            session.add(self.product)
            session.commit()
            return True
        except:
            return False

    def add_url(self, url:str) -> Boolean:
        "Add Price"
        try:
            self.product.url = url
            session.add(self.product)
            session.commit()
            return True, self.product.id
        except:
            return False, None

    def delete_product(cls, id:int) -> Boolean:
        session.query(Product).filter_by(id=id).delete()
        session.commit()

    def charge_user(cls, user:User, cost:float, wallet:str):
        admin_cut = 0.3 * cost 
        vendor_cut = 0.7 * cost

        status1 = client.send_money(
            user = user,
            amount = admin_cut,
            wallet = ADMIN_WALLET
        )

        status2 = client.send_money(
            user = user,
            amount =  vendor_cut,
            wallet = wallet
        )
        session.add(user)
        session.commit()

        return status1, status2







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
    usd_balance = client.get_balance_usd(address = user.address)
    user.balance = str(balance)
    session.add(user)
    session.commit()
    return float(usd_balance)



def get_received_msg(msg):
    "Delete This Message"

    message_id = msg.message_id
    chat = msg.chat
    return chat, message_id

def send_out_payment(user, amount, wallet):
    status = client.send_money(user, amount, wallet)
    return status
