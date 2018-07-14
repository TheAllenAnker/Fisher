# Author: Allen Anker
# Created by Allen Anker on 14/07/2018
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(20), default='Unknown')
    isbn = Column(String(15), nullable=False, unique=True)
    publisher = Column(String(50))
    pages = Column(Integer)
    pubdate = Column(String(20))
    prince = Column(String(20))
    binding = Column(String(20))
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass
