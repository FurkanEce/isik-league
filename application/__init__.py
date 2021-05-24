from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost:3306/isikleague"

db = SQLAlchemy(app)
ma = Marshmallow(app)

import application.index
import application.randevu
import application.iletisim
import application.login
import application.register
import application.profile
import application.futbol
import application.basketbol
import application.voleybol
import application.tenis
import application.amerikanFutbolu


