from flask import Flask, render_template, json, jsonify
from flask_sqlalchemy import SQLAlchemy
import urllib
import urllib.parse

app = Flask(__name__)
params = urllib.parse.quote_plus(
    "DRIVER={SQL SERVER};SERVER=DESKTOP-43GJF30;DATABASE=dsd_mazatlan;UID=sa;PWD=Dsdsistemas2012")
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vue")
def vue():
    return render_template("vue_example.html")


@app.route("/materialize")
def materialize():
    return render_template("materialize.html")


@app.route("/material")
def material():
    return render_template("material.html")


@app.route("/api/todo")
def todo():
    data = [
        {
            "id": 3,
            "title": 'Fabricas',
        },
        {
            "id": 3,
            "title": 'Fabricas',
        },
        {
            "id": 3,
            "title": 'Fabricas',
        }
    ]

    json_data = json.dumps(data)
    return json_data


@app.route("/rutas")
def mostrar_rutas():
    consulta = """SELECT 
                hu.id_ruta, hu.kilometrage_dia, rut.ruta 
                FROM historial_ubicaciones hu
                INNER JOIN cat_rutas rut ON rut.id_ruta = hu.id_ruta 
                WHERE hu.fecha_registro = '2017-01-27' AND rut.activo = 1
                ORDER BY rut.nombre"""

    rutas = db.engine.execute(consulta)
    json_data = []
    for ruta in rutas:
        c = {
            "id": ruta.id_ruta,
            "route": ruta.ruta,
            "kilometers": ruta.kilometrage_dia,
        }
        json_data.append(c)
    return jsonify(json_data)


@app.route("/cedis")
def mostrar_cedis():
    cat_cedis = db.engine.execute(
        "SELECT id_cedis, nombre FROM cat_cedis WHERE activo = 1 ORDER BY orden")
    json_cedis = []
    for cedis in cat_cedis:
        c = {
            "id": cedis.id_cedis,
            "name": cedis.nombre,
        }
        json_cedis.append(c)

    return jsonify(json_cedis)


@app.errorhandler(404)
def notFound(error):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,)
