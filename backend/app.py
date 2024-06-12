from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def inicio():
    return "Hola, Es la ruta principal"