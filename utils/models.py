import os
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()
engine = create_engine("postgresql://lqofmcthxoqgtr:de70bb56b8a237ce1b775dbd1b479e20d4f4a41c9484ede12ecfda312e5e3609@ec2-52-0-114-209.compute-1.amazonaws.com:5432/d6u5esh629cgvo")

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




# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine, autoflush=False)

session = Session()

# import pdb; pdb.set_trace()
session.close()