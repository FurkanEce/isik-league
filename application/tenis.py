from flask import Flask,render_template,session,redirect,url_for
from application import app
from application.models.tenis_model import Tenis


@app.route("/tenis")
def tenis():
    haberler = Tenis.query.filter_by(aktif = 1).all()
    oyuncular = Tenis.query.filter_by(aktif = 1).all()
   
    print(haberler[0].haberler)
    print(oyuncular[0].oyuncular)

    return render_template("tenis.html", haberler = haberler, oyuncular = oyuncular, len = len(haberler))


   