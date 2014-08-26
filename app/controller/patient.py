from flask import request, render_template
from app import app
__author__ = 'luyangsheng'


@app.route("/patient/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("patient/register.html")