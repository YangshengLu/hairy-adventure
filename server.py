# -*- coding: utf8 -*-
__author__ = 'luyangsheng'

import tornado.ioloop
import tornado.web
import tornado.log
import setting


app = tornado.web.Application(
    setting.urls,
    setting.options
)

if __name__ == "__main__":
    app.listen(port=12306)
    tornado.ioloop.IOLoop.instance().start()