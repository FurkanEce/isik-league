from flask import Flask,render_template,session,redirect,url_for
from application import app


@app.route("/")
@app.route("/anasayfa")
def index():
    return render_template("index.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))