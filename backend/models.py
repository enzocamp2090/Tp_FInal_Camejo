from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Usuario(db.Model):
    __tablename__='usuarios'
    id = db.Column(db.Integrer, primary_key=True)
    