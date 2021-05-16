from flask import Flask,render_template, session
from application import app
from application.models.randevu_model import Randevu


@app.route("/profile")
def profile():

    user_id = session["user_id"]
    randevular = Randevu.query.filter_by(kullanici_id = user_id).all()
    

    return render_template("profile.html", randevular = randevular)

    