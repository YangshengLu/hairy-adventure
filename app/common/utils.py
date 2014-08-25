# coding=utf-8

__author__ = 'luyangsheng'

import hashlib
from app import options


def pass_crypto(plain):
    plain = plain + options['SECRET_KEY']
    sha1 = hashlib.sha1()
    sha1.update(plain)
    return sha1.hexdigest()