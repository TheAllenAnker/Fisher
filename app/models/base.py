# Author: Allen Anker
# Created by Allen Anker on 18/07/2018
from sqlalchemy import Column, SmallInteger
from flask_sqlalchemy import SQLAlchemy

__all__ = ['db', 'Base']


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
