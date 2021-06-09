from flask import Flask,render_template,session,redirect,url_for
from application import app
from application.models.voleybol_model import Voleybol


@app.route("/voleybol")
def voleybol():
    haberler = Voleybol.query.filter_by(aktif = 1).all()
    oyuncular = Voleybol.query.filter_by(aktif = 1).all()
   
    print(haberler[0].haberler)
    print(oyuncular[0].oyuncular)

    return render_template("voleybol.html", haberler = haberler, oyuncular = oyuncular, len = len(haberler),len2 = len(oyuncular))
