# -＊- coding: utf8 -*-
__author__ = 'luyangsheng'
from sqlalchemy.ext.declarative import declarative_base
from setting import engine
from sqlalchemy import Column, String, Integer, Float, Enum

Base = declarative_base(engine)


class Admin(Base):

    __tablename__ = 'db_sys_admin'

    username = Column(String(length=20))
    password = Column(String(length=32))


class Medicine(Base):

    __tablename__ = "medicine"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50), nullable=False)
    price = Column(Float, nullable=False)
    unit = Column(String(length=5), nullable=False)
    desc = Column(String(length=200), nullable=True)


class Doctor(Base):

    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_card_num = Column(String(length=18), nullable=False)
    name = Column(String(length=50), nullable=False)
    gender = Column(Enum(('男', '女')))
    department = Column(String(length=20), nullable=False)
    tel = Column(String(length=20), nullable=False)


class SickRoom(Base):

    __tablename__ = "sick_room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(length=100), unique=True)


class Patient(Base):

    __tablename = "patient"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_card_num = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(length=50), nullable=False)
    gender = Column(String(length=1), nullable=False)
    tel = Column(String(length=20), nullable=False)


Base.metadata.create_all()