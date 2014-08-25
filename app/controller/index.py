import logging
from flask import render_template
from app import app
from flask import session

__author__ = 'luyangsheng'


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