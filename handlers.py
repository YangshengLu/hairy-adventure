__author__ = 'luyangsheng'
import tornado.web
import logging


class BaseRequesetHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        super(BaseRequesetHandler, self).get_current_user()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.set_secure_cookie("__hsp_cookie", ("10010", 123))
        self.write("首页")

    def post(self):
        try:
            hello = self.get_body_argument("hello")
        except tornado.web.MissingArgumentError as e:
            logging.exception(e)
        print(hello)
        self.write(hello)