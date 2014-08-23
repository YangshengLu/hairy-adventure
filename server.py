__author__ = 'luyangsheng'

import tornado.ioloop
import tornado.web
import tornado.log
import logging
import json
import mysql.connector


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("首页")

    def post(self):
        try:
            hello = self.get_body_argument("hello")
        except tornado.web.MissingArgumentError as e:
            logging.exception(e)
        print(hello)
        self.write(hello)

app = tornado.web.Application([
    (r'/', MainHandler),
])

if __name__ == "__main__":
    app.listen(port=12306)
    tornado.ioloop.IOLoop.instance().start()