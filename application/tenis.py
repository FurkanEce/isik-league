from flask import Flask,render_template,session,redirect,url_for
from application import app



@app.route("/tenis")
def tenis():
    return render_template("tenis.html")