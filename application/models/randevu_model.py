from application import db
from datetime import datetime


class Randevu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kullanici_id = db.Column(db.Integer, primary_keys=True)
    saat = db.Column(db.String, nullable=False)
    aktif_randevu = db.Column(db.Boolean, default=True, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    tarih = db.Column(db.String, nullable=False)
    saha = db.Column(db.Integer, nullable=False)