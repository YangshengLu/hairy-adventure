from flask import request, render_template
from app import app
__author__ = 'luyangsheng'


@app.route("/patient_register", methods=["GET", "POST"])
def patient_register():
    if request.method == "GET":
        return render_template("patient_register.html")