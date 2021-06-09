from application import db
from datetime import datetime


class Afutbol(db.Model):
    idamerikanFutbolu = db.Column(db.Integer, primary_key=True)
    haberler = db.Column(db.Integer, primary_keys=True)
    aktif = db.Column(db.Boolean, default=True, nullable=False)
    oyuncular = db.Column(db.String, primary_keys=True)
    gorev = db.Column(db.String, primary_keys=True)
    bolum = db.Column(db.String, primary_keys=True)