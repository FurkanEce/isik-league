from flask import Flask,render_template,session,redirect,url_for
from application import app
from application.models.futbol_model import Futbol



@app.route("/futbol")
def futbol():

    
    haberler = Futbol.query.filter_by(aktif = 1).all()
    oyuncular = Futbol.query.filter_by(aktif = 1).all()
   
    print(haberler[0].haberler)
    print(oyuncular[0].oyuncular)

    return render_template("futbol.html", haberler = haberler, oyuncular = oyuncular, len = len(haberler),len2 = len(oyuncular))