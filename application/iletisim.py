from flask import Flask,render_template
from application import app


@app.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")