from flask import Flask, render_template, json, jsonify
from flask_sqlalchemy import SQLAlchemy
import urllib
import urllib.parse

app = Flask(__name__)
params = urllib.parse.quote_plus("DRIVER={SQL SERVER};SERVER=DESKTOP-43GJF30;DATABASE=dsd_mazatlan;UID=sa;PWD=Dsdsistemas2012")
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


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
    rutas = db.engine.execute("SELECT id_ruta, nombre FROM cat_rutas WHERE activo = 1 AND nombre >= 100")
    json_data = []
    for ruta in rutas:
        c = {
            "id": ruta.id_ruta,
            "nombre": ruta.nombre,
        }
        json_data.append(c)
    
    cat_cedis = db.engine.execute("SELECT id_cedis, nombre FROM cat_cedis WHERE activo = 1")
    json_cedis = []
    for cedis in cat_cedis:
        c = {
            "id": cedis.id_cedis,
            "nombre": cedis.nombre,
        }
        json_cedis.append(c)

    return jsonify({"rutas": json_data},{"cedis":json_cedis})

@app.errorhandler(404)
def notFound(error):
    return render_template("404.html"),404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,)
