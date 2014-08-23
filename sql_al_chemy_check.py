# -*- coding: utf-8 -*-
__author__ = 'luyangsheng'

from sqlalchemy import create_engine, Column, Integer, String, FLOAT
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqlconnector://root:root@localhost/db_sys?charset=utf8", encoding='utf8', echo=True)
Base = declarative_base(engine)
Session = sessionmaker(bind=engine)


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    price = Column(FLOAT)

    def __repr__(self):
        return "<Book, id=%s, name=%s, price=%s>" % (self.id, self.name, self.price)

Base.metadata.create_all(engine)


session = Session()

result = session.query(Book).filter(Book.id == 5)
if result and result.count():
    instance = result[0]
    instance.name = u"百度知道"
else:
    instance = Book(name=u"是的发", price=20.1)
session.add(instance)
session.commit()

print(instance.name)

