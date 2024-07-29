from models import db, Babosos, Datos_baboso
from flask import Flask, request, jsonify
from models import db, Babosos, Datos_baboso
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.run(debug=True)
port = 5000
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://enzo:121629@localhost:5432/babosos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
        return jsonify({'mensaje': 'Error del servidor'}), 500

@app.route("/babosos/<id_baboso>", methods=["GET", "DELETE", "PUT"])
def nuevo_baboso(id_baboso):
    baboso = Datos_baboso.query.where(Datos_baboso.id == id_baboso).first()
    if request.method == 'GET':
        baboso_data = {
            "nombre": baboso.nombre, 
            "encuentro": baboso.encuentro, 
            "tiempo_declaracion" : baboso.tiempo_declaracion, 
            "aparicion" : baboso.aparicion, 
            "frase_ingeniosa": baboso.frase_ingeniosa, 
            "respuesta" : baboso.respuesta, 
            "prop_indecentes" : baboso.prop_indecentes, 
            "prop_previsibles" : baboso.prop_previsibles, 
            "prop_divertidas" : baboso.prop_divertidas, 
            "voto_autoestima" : baboso.voto_autoestima, 
            "voto_insistente" : baboso.voto_insistente, 
            "voto_originalidad" : baboso.voto_originalidad, 
            "conclusion" : baboso.conclusion
            }
        return baboso_data
    elif request.method == 'DELETE':
        baboso_delete = Datos_baboso.query.get(id_baboso)
        db.session.delete(baboso_delete)
        db.session.commit()
        return jsonify({"Mensaje": "Baboso eliminado"}), 200
    elif request.method == 'PUT':
        data_baboso = request.get_json()
        baboso.nombre = data_baboso['nombre'], 
        baboso.encuentro = data_baboso['encuentro'], 
        baboso.tiempo_declaracion = data_baboso['tiempo_declaracion'], 
        baboso.aparicion = data_baboso['aparicion'], 
        baboso.frase_ingeniosa =  data_baboso['frase_ingeniosa'], 
        baboso.espuesta = data_baboso['respuesta'], 
        baboso.prop_indecentes = data_baboso['prop_indecentes'], 
        baboso.prop_previsibles = data_baboso['prop_previsibles'], 
        baboso.prop_divertidas = data_baboso['prop_divertidas'], 
        baboso.voto_autoestima = data_baboso['voto_autoestima'], 
        baboso.voto_insistente = data_baboso['voto_insistente'], 
        baboso.voto_originalidad = data_baboso['voto_originalidad'], 
        baboso.conclusion = data_baboso['conclusion']
        db.session.commit()
        return jsonify({"id": baboso.baboso_id, "nombre" : baboso.nombre}), 200

