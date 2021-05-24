from flask import Flask,render_template,session,redirect,url_for
from application import app



@app.route("/basketbol")
def basketbol():
    return render_template("basketbol.html")