__author__ = 'luyangsheng'
from sqlalchemy import create_engine

__database_config__ = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "db_sys",
}
__DATABASE_URL_FORMAT__ = "mysql+mysqlconnector://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s"


__db_url = __DATABASE_URL_FORMAT__ % __database_config__
engine = create_engine(__db_url, encoding="utf8", echo=False)

