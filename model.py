from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

from config import *

Base = declarative_base()
engine = create_engine(
    os.getenv("DATABASE_URL"),
    echo=False
)



class User(Base):
    """
    SqlAlchemy ORM for Users
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    balance = Column(String(10))
    orders = Column(Integer)
    wallet = Column(String(32))

    def __repr__(self):
        return "<User(id='%s')>" % (self.id)


# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine, autoflush=False)

session = Session()

# import pdb; pdb.set_trace()
session.close()