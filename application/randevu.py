from flask import Flask,render_template,request,session,redirect,url_for
from application import app,db
from application.models.randevu_model import Randevu
from datetime import datetime


@app.route("/randevu", methods=['GET'])
def randevu():
    formatted_randevular = {}
    for key in range(0, 24):
        if key < 10:
            formatted_randevular['0{}:00'.format(key)] = 0
        else:
            formatted_randevular['{}:00'.format(key)] = 0
    today_date = datetime.now()
    change_date = today_date.strftime("%Y-%m-%d")
    randevular = Randevu.query.filter_by(tarih = change_date, saha=1).all()
    for randevu in randevular:
        formatted_randevular[randevu.saat] = randevu.aktif_randevu
    return render_template("randevu.html", randevu = formatted_randevular, tarih = change_date, saha="1")

@app.route("/randevu/<string:saha>/<string:tarih>", methods=['GET'])
def randevuye_git(saha, tarih):
    today_date = datetime.now()
    change_date = today_date.strftime("%Y-%m-%d")
    if tarih < change_date:
        tarih = change_date
    formatted_randevular = {}
    for key in range(0, 24):
        if key < 10:
            formatted_randevular['0{}:00'.format(key)] = 0
        else:
            formatted_randevular['{}:00'.format(key)] = 0
    randevular = Randevu.query.filter_by(tarih = tarih, saha=int(saha)).all()
    for randevu in randevular:
        formatted_randevular[randevu.saat] = randevu.aktif_randevu
    return render_template("randevu.html", randevu = formatted_randevular, tarih = tarih, saha=saha)


@app.route('/randevu/kaydet', methods=['POST'])
def kaydet():
    user_id = session["user_id"]
    tarih = request.form['tarih']
    saat = request.form['saat']
    saha = request.form['saha']
    randevu = Randevu(saat = saat, tarih=tarih, kullanici_id = user_id, saha = int(saha))
    db.session.add(randevu)
    db.session.commit()
    return redirect(url_for("profile"))


@app.route('/randevu/sil/<string:id>')
def sil(id):
    randevu = Randevu.query.get(id)
    db.session.delete(randevu)
    db.session.commit()
    return redirect(url_for("profile"))    

    


    