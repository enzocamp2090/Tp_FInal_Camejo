from models import db, Usuario, Babosos, Datos_baboso
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
port = 5000
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql+psycopg2://enzo:121629@localhost:5432/babosos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route("/")
def inicio():
    return "Hola, Es la ruta principal"

if __name__ == '__main__':
    print('Starting server.....')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started...')