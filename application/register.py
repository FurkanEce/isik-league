from flask import Flask,render_template,request,redirect,url_for
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from application.models.kullanici_model import Kullanici
from application import app, db


#Kayıt Olma
@app.route("/kayıtOl",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        db.create_all()
        kullanici = Kullanici(isim_soyisim = name, kullanici_adi = username, email = email, sifre = password )
        db.session.add(kullanici)
        db.session.commit()
        
        return redirect(url_for("login"))
    else:
        print("hello")
        return render_template("register.html",form = form)


# Kullanıcı Kayıt Formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim",validators=[validators.Length(min = 4,max = 25)])
    username = StringField("Kullanıcı Adı",validators=[validators.Length(min = 5,max = 35)])
    email = StringField("Email Adresi",validators=[validators.Email(message = "Lütfen Geçerli Bir Email Adresi Girin...")])
    password = PasswordField("Parola:",validators=[
        validators.DataRequired(message = "Lütfen bir parola belirleyin"),
        validators.EqualTo(fieldname = "confirm",message="Parolanız Uyuşmuyor...")
    ])
    confirm = PasswordField("Parola Doğrula")