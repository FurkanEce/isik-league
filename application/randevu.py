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
    randevular = Randevu.query.filter_by(tarih = change_date).all()
    for randevu in randevular:
        formatted_randevular[randevu.saat] = randevu.aktif_randevu
    return render_template("randevu.html", randevu = formatted_randevular, tarih = change_date)

@app.route("/randevu/<string:tarih>", methods=['GET'])
def randevuye_git(tarih):
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
    randevular = Randevu.query.filter_by(tarih = tarih).all()
    for randevu in randevular:
        formatted_randevular[randevu.saat] = randevu.aktif_randevu
    return render_template("randevu.html", randevu = formatted_randevular, tarih = tarih)


@app.route('/randevu/kaydet', methods=['POST'])
def kaydet():
    user_id = session["user_id"]
    tarih = request.form['tarih']
    saat = request.form['saat']
    randevu = Randevu(saat = saat, tarih=tarih, kullanici_id = user_id)
    db.session.add(randevu)
    db.session.commit()
    return redirect(url_for("profile"))


@app.route('/randevu/sil/<string:id>')
def sil(id):
    randevu = Randevu.query.get(id)
    db.session.delete(randevu)
    db.session.commit()
    return redirect(url_for("profile"))    

    


    