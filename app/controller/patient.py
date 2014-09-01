# coding=utf-8
from flask import request, render_template
from app import app
__author__ = 'luyangsheng'


@app.route("/patient/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("patient/register.html")
    elif request.method == "POST":
        try:
            id_card_num = int(request.form["id_card_num"])
            name = str(request.form['name'])
            gender = str(request.form['gender'])
            if gender not in ("男", "女"):
                raise KeyError

        except KeyError:
            pass