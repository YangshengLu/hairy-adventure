__author__ = 'luyangsheng'
from flask import Flask
from flask import render_template, request, session, g
from flask.sessions import SessionInterface
import setting
from setting import logging
from beaker.middleware import SessionMiddleware

app = Flask(__name__)
app.config.update(**setting.options)


class BeakerSessionInterface(SessionInterface):

    def open_session(self, _app, _request):
        _session = request.environ['beaker.session']
        return _session

    def save_session(self, _app, _session, response):
        _session.save()


# initial database session before request
@app.before_request
def before_request():
    g.db_session = setting.Session()


# close database session after request
@app.teardown_request
def teardnow_request(exception):
    if exception:
        app.logger.exception(exception)
    if g.db_session:
        try:
            g.db_session.close()
        except Exception as e:
            app.logger.exception(e)


@app.route("/", methods=["GET", "POST"])
def index():
    session['pid'] = 200
    result = {
        "hello": 100
    }
    return render_template("index.html", **result)


@app.route("/log_test", methods=["GET"])
def log_test():
    logger = logging.getLogger(__name__)
    logger.info("logger")
    return 'hello'


if __name__ == "__main__":
    app.wsgi_app = SessionMiddleware(
        app.wsgi_app,
        setting.session_opts,
        **setting.session_setting
    )
    app.session_interface = BeakerSessionInterface()
    app.run(port=12306, debug=True)