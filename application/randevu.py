from flask import Flask,render_template,request,session,redirect,url_for
from application import app, db
from application.models.randevu_model import Randevu
from datetime import datetime


@app.route("/randevu", methods=['GET'])
def randevu():
    return render_template("randevu.html")


@app.route('/randevu/kaydet', methods=['POST'])
def kaydet():
    user_id =  session["user_id"]
    time = request.form['time']
    new_time = datetime.strptime(time, '%m/%d/%Y %H:%M %p')
    db.create_all()
    randevu = Randevu(saat = new_time, kullanici_id = user_id)
    db.session.add(randevu)
    db.session.commit()
    return time

@app.route('/randevu/sil/<string:id>')
def sil(id):
    randevu = Randevu.query.get(id)
    db.session.delete(randevu)
    db.session.commit()
    return redirect(url_for("profile"))    

    


    