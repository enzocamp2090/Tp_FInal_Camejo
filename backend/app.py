from flask import Flask, request, jsonify
from models import db, Baboso, DatosBaboso
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://mariana:212124@localhost:5432/babosos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def inicio():
    return "Hola, Es la ruta principal"

@app.route("/babosos", methods=["GET"])
def data():
    try:
        babosos = Baboso.query.all()
        print(babosos)
        babosos_data = []
        for baboso in babosos:
            baboso_data = {
                "id": baboso.id,
                "nombre": baboso.nombre,
                "datos_baboso_id": baboso.datos_baboso_id
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
        print("Datos recibidos:", data)
        nombre = data.get('nombre')
        lugar_acercamiento = data.get('lugar_acercamiento')
        tiempo_declararse = data.get('tiempo_declararse')
        forma = data.get('forma')
        frase = data.get('frase')
        respuesta = data.get('respuesta')
        indecentes = data.get('indecentes')
        previsibles = data.get('previsibles')
        divertidos = data.get('divertidos')
        autoestima = data.get('autoestima')
        insistencia = data.get('insistencia')
        originalidad = data.get('originalidad')
        veredicto = data.get('veredicto')

        nuevo_dato_baboso = DatosBaboso(
            nombre=nombre, 
            lugar_acercamiento=lugar_acercamiento, 
            tiempo_declararse=tiempo_declararse, 
            forma=forma, 
            frase=frase, 
            respuesta=respuesta, 
            indecentes=indecentes, 
            previsibles=previsibles, 
            divertidos=divertidos, 
            autoestima=autoestima, 
            insistencia=insistencia, 
            originalidad=originalidad, 
            veredicto=veredicto
        )

        db.session.add(nuevo_dato_baboso)
        db.session.commit()

        print(f"ID del nuevo dato baboso: {nuevo_dato_baboso.id}")

        nuevo_baboso = Baboso(
            nombre=nombre,
            datos_baboso_id=nuevo_dato_baboso.id  # Ajustado para usar datos_baboso_id
        )

        db.session.add(nuevo_baboso)
        db.session.commit()

        return jsonify({'id': nuevo_dato_baboso.id, 'nombre': nuevo_dato_baboso.nombre})
    except Exception as e:
        db.session.rollback()
        print("Error al guardar el baboso:", e)
        return jsonify({'error': str(e)}), 500

@app.route("/babosos/<id>", methods=["GET", "DELETE", "PUT"])
def nuevo_baboso_id(id):
    dato_baboso = DatosBaboso.query.where(DatosBaboso.id == id).first()
    baboso = Baboso.query.where(Baboso.datos_baboso_id == id).first()
    if request.method == 'GET':
        baboso_data = {
            "nombre": dato_baboso.nombre, 
            "lugar_acercamiento": dato_baboso.lugar_acercamiento, 
            "tiempo_declararse" : dato_baboso.tiempo_declararse, 
            "forma" : dato_baboso.forma, 
            "frase": dato_baboso.frase, 
            "respuesta" : dato_baboso.respuesta, 
            "indecentes" : dato_baboso.indecentes, 
            "previsibles" : dato_baboso.previsibles, 
            "divertidos" : dato_baboso.divertidos, 
            "autoestima" : dato_baboso.autoestima, 
            "insistencia" : dato_baboso.insistencia, 
            "originalidad" : dato_baboso.originalidad, 
            "veredicto" : dato_baboso.veredicto
            }
        return baboso_data
    elif request.method == 'DELETE':
        baboso_delete = DatosBaboso.query.get(id)
        db.session.delete(baboso_delete)
        db.session.commit()
        return jsonify({"Mensaje": "Baboso eliminado"}), 200
    elif request.method == 'PUT':
        data_baboso = request.get_json()
        dato_baboso.nombre = data_baboso['nombre'], 
        dato_baboso.lugar_acercamiento = data_baboso['lugar_acercamiento'], 
        dato_baboso.tiempo_declararse = data_baboso['tiempo_declararse'], 
        dato_baboso.forma = data_baboso['forma'], 
        dato_baboso.frase =  data_baboso['frase'], 
        dato_baboso.respuesta = data_baboso['respuesta'], 
        dato_baboso.indecentes = data_baboso['indecentes'], 
        dato_baboso.previsibles = data_baboso['previsibles'], 
        dato_baboso.divertidos = data_baboso['divertidos'], 
        dato_baboso.autoestima = data_baboso['autoestima'], 
        dato_baboso.insistencia = data_baboso['insistencia'], 
        dato_baboso.originalidad = data_baboso['originalidad'], 
        dato_baboso.veredicto = data_baboso['veredicto']

        baboso.nombre = data_baboso['nombre']

        db.session.commit()
        return jsonify({"id": id, "nombre" : dato_baboso.nombre}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)