# coding=utf-8
__author__ = 'luyangsheng'
from sqlalchemy.ext.declarative import declarative_base as _declarative_base
from sqlalchemy import Column, String, Integer as Integer, Float, Enum as Enum

from app import engine
_Base = _declarative_base(engine)


class Admin(_Base):

    __tablename__ = 'db_sys_admin'

    username = Column(String(length=20), primary_key=True)
    password = Column(String(length=32), nullable=False)


class Medicine(_Base):

    __tablename__ = "medicine"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    price = Column(Float, nullable=False)
    unit = Column(String(length=5), nullable=False)
    desc = Column(String(length=200), nullable=True)


class Doctor(_Base):

    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_card_num = Column(String(length=18), nullable=False)
    name = Column(String(length=50), nullable=False)
    gender = Column(Enum(u'男', u'女'))
    department = Column(String(length=20), nullable=False)
    tel = Column(String(length=20), nullable=False)


class SickRoom(_Base):

    __tablename__ = "sick_room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(length=100), unique=True)


class Patient(_Base):

    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_card_num = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=50), nullable=False)
    gender = Column(String(length=1), nullable=False)
    tel = Column(String(length=20), nullable=False)


_Base.metadata.create_all()
