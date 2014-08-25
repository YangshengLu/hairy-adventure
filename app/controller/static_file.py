from flask import send_from_directory
from app import app

__author__ = 'luyangsheng'


# static file config
@app.route("/css/<path:filename>")
def css_static(filename):
    return send_from_directory("static/css", filename)


@app.route("/js/<path:filename>")
def js_static(filename):
    return send_from_directory("static/js", filename)


@app.route("/fonts/<path:filename>")
def fonts_static(filename):
    return send_from_directory("static/fonts", filename)