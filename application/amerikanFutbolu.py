from flask import Flask,render_template,session,redirect,url_for
from application import app



@app.route("/amerikanFutbolu")
def amerikanFutbolu():
    return render_template("amerikanFutbolu.html")