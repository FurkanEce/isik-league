from flask import Flask,render_template,request,flash,redirect,url_for,session
from application import app,db
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from application.models.kullanici_model import Kullanici


@app.route("/giris",methods =["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
       username = form.username.data
       password_entered = form.password.data
       user = Kullanici.query.filter_by(kullanici_adi = username).first()
       if user:
           if user.sifre == password_entered:
               flash("Başarıyla Giriş Yaptınız...","success")

               session["logged_in"] = True
               session["username"] = username
               session["user_id"] = user.id
               session["email"] = user.email
               
               return redirect(url_for("index"))
           else:

               flash("Parolanızı Yanlış Girdiniz...","danger")
               return redirect(url_for("login")) 

       else:
           flash("Böyle bir kullanıcı bulunmuyor...","danger")
           return redirect(url_for("login"))

    
    return render_template("login.html",form = form)


class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("Parola")