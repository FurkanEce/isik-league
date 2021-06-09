from flask import Flask,render_template,session,redirect,url_for
from application import app
from application.models.basketbol_model import Basketbol


@app.route("/basketbol")
def basketbol():
    haberler = Basketbol.query.filter_by(aktif = 1).all()
    oyuncular = Basketbol.query.filter_by(aktif = 1).all()
   
    print(haberler[0].haberler)
    print(oyuncular[0].oyuncular)

    return render_template("basketbol.html", haberler = haberler, oyuncular = oyuncular, len = len(haberler),len2 = len(oyuncular))
