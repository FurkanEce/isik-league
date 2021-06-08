from flask import Flask,render_template,request,session,redirect,url_for
from application import app,db
from application.models.randevu_model import Randevu
from application.models.kullanici_model import Kullanici
from datetime import datetime
from flask_mail import Mail, Message


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'furkanece99@gmail.com'
app.config['MAIL_PASSWORD'] = 'Pinar123.'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

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
    email = session["email"]
    gonder = Kullanici.query.filter_by(email = email).first()
    print(gonder)
    randevu = Randevu(saat = saat, tarih=tarih, kullanici_id = user_id, saha = int(saha))
    print(randevu)
    db.session.add(randevu)
    db.session.commit()
    msg = Message('Randevunuz Oluşturulmuştur', sender = 'furkanece99@gmail.com', recipients = [gonder.email])
    msg.body = "Saat "+ randevu.saat +"'ya "+ str(randevu.saha) +" numaralı saha için randevunuz oluşturulmuştur iyi eğlenceler."
    mail.send(msg)
    print(msg)
    return redirect(url_for("profile"))
    
    


@app.route('/randevu/sil/<string:id>')
def sil(id):
    email = session["email"]
    gonder = Kullanici.query.filter_by(email = email).first()
    randevu = Randevu.query.get(id)
    db.session.delete(randevu)
    db.session.commit()
    msg = Message('Randevunuz İptal Edilmiştir', sender = 'furkanece99@gmail.com', recipients = [gonder.email])
    msg.body = "Saat "+ randevu.saat +"'ya "+ str(randevu.saha) +" numaralı saha için alınan randevunuz iptal edilmiştir."
    mail.send(msg)
    print(msg)
    return redirect(url_for("profile"))    

    


    