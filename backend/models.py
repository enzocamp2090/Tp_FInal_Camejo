from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DatosBaboso(db.Model):
    __tablename__ = 'datos_baboso'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    lugar_acercamiento = db.Column(db.String(255), nullable=False)
    tiempo_declararse = db.Column(db.String(255), nullable=False)
    forma = db.Column(db.String(255), nullable=False)
    frase = db.Column(db.String(255), nullable=False)
    respuesta = db.Column(db.String(255), nullable=False)
    indecentes = db.Column(db.String(255), nullable=False)
    previsibles = db.Column(db.String(255), nullable=False)
    divertidos = db.Column(db.String(255), nullable=False)
    autoestima = db.Column(db.Integer, nullable=False)
    insistencia = db.Column(db.Integer, nullable=False)
    originalidad = db.Column(db.Integer, nullable=False)
    veredicto = db.Column(db.String(255), nullable=False)
    baboso = db.relationship('Baboso', back_populates='datos_baboso', cascade='all, delete-orphan')

class Baboso(db.Model):
    __tablename__ = 'baboso'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    datos_baboso_id = db.Column(db.Integer, db.ForeignKey('datos_baboso.id'), nullable=False)
    datos_baboso = db.relationship('DatosBaboso', back_populates='baboso')