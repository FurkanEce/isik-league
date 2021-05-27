from application import db
from datetime import datetime


class Voleybol(db.Model):
    idvoleybol = db.Column(db.Integer, primary_key=True)
    haberler = db.Column(db.Integer, primary_keys=True)
    aktif = db.Column(db.Boolean, default=True, nullable=False)
    oyuncular = db.Column(db.String, primary_keys=True)