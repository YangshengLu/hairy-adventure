# -*- coding: utf8 -*-
__author__ = 'luyangsheng'
from sqlalchemy import create_engine
import handlers


# database settings
__DB_URL_FORMAT__ = "mysql+mysqlconnector://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s"
__db_config__ = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "db_sys",
}
engine = create_engine(
    __DB_URL_FORMAT__ % __db_config__,
    encoding="utf8",
    echo=False
)


# url map setting
urls = (
    (r'/', handlers.MainHandler),
)


# other sever options
options = {
    "cookie_secret": "3087c29ddaaed0a7671093b3eb00ad4a",
}