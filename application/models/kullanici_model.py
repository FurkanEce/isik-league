from application import db
from passlib.hash import sha256_crypt

class Kullanici(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isim_soyisim = db.Column(db.String(45))
    kullanici_adi = db.Column(db.String(45))
    email = db.Column(db.String(45))
    sifre = db.Column(db.String(45))