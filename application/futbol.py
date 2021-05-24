from flask import Flask,render_template,session,redirect,url_for
from application import app



@app.route("/futbol")
def futbol():
    return render_template("futbol.html")