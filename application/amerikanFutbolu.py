from flask import Flask,render_template,session,redirect,url_for
from application import app
from application.models.amerikanFutbolu_model import Afutbol



@app.route("/amerikanFutbolu")
def amerikanFutbolu():
    haberler = Afutbol.query.filter_by(aktif = 1).all()
    oyuncular = Afutbol.query.filter_by(aktif = 1).all()
   
    print(haberler[0].haberler)
    print(oyuncular[0].oyuncular)

    return render_template("amerikanFutbolu.html", haberler = haberler, oyuncular = oyuncular, len = len(haberler))
