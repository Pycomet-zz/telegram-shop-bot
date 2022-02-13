from config import *
from itertools import product
import os
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()
engine = create_engine(
    DATABASE_URL,
    echo=False)

class User(Base):
    """
    SqlAlchemy ORM for Users
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    balance = Column(String(15))
    orders = Column(Integer)
    address = Column(String(50))
    mnemonic = Column(String(100))

    def __repr__(self):
        return "<User(id='%s')>" % (self.id)



class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)
    address = Column(String(50))
    mnemonic = Column(String(200))
    xpub = Column(String(200))



class Product(Base):
    __tablename__ = "products"

    id = Column(String(16), primary_key=True)
    owner = Column(Integer)
    name = Column(String(20))
    category = Column(String(20))
    subcategory = Column(String(20))
    desc = Column(String(500))
    price = Column(Integer)
    url = Column(String(100))
    orders = relationship("Order", cascade="all, delete-orphan")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    cost = Column(String(50))
    product_id =  Column(ForeignKey("products.id", ondelete="CASCADE"))
    product = relationship("Product", uselist=False)




# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine, autoflush=False)

session = Session()

# import pdb; pdb.set_trace()
session.close()