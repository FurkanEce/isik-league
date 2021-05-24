from flask import Flask,render_template,session,redirect,url_for
from application import app



@app.route("/voleybol")
def voleybol():
    return render_template("voleybol.html")