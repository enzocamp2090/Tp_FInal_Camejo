from models import db, Babosos, Datos_baboso
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
port = 5000
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://enzo:121629@localhost:5432/babosos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def inicio():
    return "Hola, Es la ruta principal"

@app.route("/babosos", methods=["GET"])
def data():
    try:
        babosos = Babosos.query.all()
        babosos_data = []
        for baboso in babosos:
            baboso_data = {
                "id": baboso.id_baboso,
                "nombre": baboso.nombre,
            }
            babosos_data.append(baboso_data)
        return jsonify(babosos_data)
    except:
        print("erorr")
        return jsonify({"mensaje": "no existe el baboso"}), 500
        
@app.route("/babosos", methods=["POST"])
def nuevo_baboso():
    try:
        data = request.json
        nombre = data.get('nombre')
        encuentro = data.get('lugar_acercamiento')
        tiempo_declaracion = data.get('tiempo_declararse')
        aparicion = data.get('forma')
        frase_ingeniosa = data.get('frase_ingeniosa')
        respuesta = data.get('respuesta')
        prop_indecentes = data.get('indecentes')
        prop_previsibles = data.get('previsibles')
        prop_divertidas = data.get('divertidos')
        voto_autoestima = data.get('autoestima')
        voto_insistente = data.get('insistencia')
        voto_originalidad = data.get('originalidad')
        conclusion = data.get('veredicto')

        nuevo_baboso = Datos_baboso(
            nombre=nombre, 
            encuentro=encuentro, 
            tiempo_declaracion=tiempo_declaracion, 
            aparicion=aparicion, 
            frase_ingeniosa=frase_ingeniosa, 
            respuesta=respuesta, 
            prop_indecentes=prop_indecentes, 
            prop_previsibles=prop_previsibles, 
            prop_divertidas=prop_divertidas, 
            voto_autoestima=voto_autoestima, 
            voto_insistente=voto_insistente, 
            voto_originalidad=voto_originalidad, 
            conclusion=conclusion
        )
        db.session.add(nuevo_baboso)
        db.session.commit()
        return jsonify({'id': nuevo_baboso.id, 'nombre': nuevo_baboso.nombre})
    except Exception:
        print("erorr")
        return jsonify({'message': 'internal server error'}), 500
