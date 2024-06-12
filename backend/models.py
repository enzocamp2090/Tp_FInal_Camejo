import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Usuario(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(255), nullable=False)
    contraena = db.Column(db.String(255), nullable=False)

class Babosos(db.Model):
    __tablename__='babosos'
    id_baboso = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    apodo = db.Column(db.String(255), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.now())

class Datos_baboso(db.Model):
    __tablename__='baboso'
    id =db.Column(db.Integer, primary_key=True)
    id_baboso = db.Column(db.Integer,db.ForeignKey('babosos.id_baboso'))
    nombre = db.Column(db.String(255), nullable=False)
    encuentro = db.Column(db.String(255), nullable=False)
    tiempo_declaracion = db.Column(db.String(255), nullable=False)
    aparicion = db.Column(db.String(255), nullable=False)
    frase_ingeniosa = db.Column(db.String(255), nullable=False)
    respuesta = db.Column(db.String(255), nullable=False)
    prop_indecentes = db.Column(db.Integer, nullable=False)
    prop_previsibles = db.Column(db.Integer, nullable=False)
    prop_divertidas = db.Column(db.Integer, nullable=False)
    voto_autoestima = db.Column(db.Integer, nullable=False)
    voto_insistente = db.Column(db.Integer, nullable=False)
    voto_originalidad = db.Column(db.Integer, nullable=False)
    dibujo = db.Column(db.String(255), nullable=False)
    conclusion = db.Column(db.String(255), nullable=False)