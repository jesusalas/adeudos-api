from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import pyodbc
import urllib
import urllib.parse

app = Flask(__name__, static_url_path='/static')
params = urllib.parse.quote_plus(
    "DRIVER={SQL SERVER};SERVER=172.16.1.2;DATABASE=dsd_mazatlan;UID=sa;PWD=Dsdsistemas2012")
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
db = SQLAlchemy(app)


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    def __init__(self, title="", description=""):
        self.title = title
        self.description = description

    def __repr__(self):
        return 'Ruta: %s' % self.title


class RoutePoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.Integer, db.ForeignKey('route.id'))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __init__(self, route, lat, lng):
        self.route = route
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return 'lat: %s - lng: %s' % (self.lat, self.lng)


class Cat_bancos(db.Model):
    id_banco = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    clave_fiscal = db.Column(db.String)
    pagina_web = db.Column(db.String)
    fecha_registro = db.Column(db.Date)
    usuario_registro = db.Column(db.Integer)
    activo = db.Column(db.Integer)
    cuenta_contable = db.Column(db.String)

    def __init__(self, nombre, clave_fiscal, pagina_web, fecha_registro, usuario_registro, activo, cuenta_contable):
        self.nombre = nombre
        self.clave_fiscal = clave_fiscal
        self.pagina_web = pagina_web
        self.fecha_registro = fecha_registro
        self.usuario_registro = usuario_registro
        self.activo = activo
        self.cuenta_contable = cuenta_contable


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/rutas")
def rutas():
    return render_template("rutas.html")


@app.route("/api/routes/")
def show_routes():
    routes = Route.query.all()
    json_data = []
    for route in routes:
        r = {
            "title": route.title,
            "descripcion": route.description,
        }
        json_data.append(r)
    return jsonify({"routes": json_data})


@app.route("/api/banks/")
def show_banks():
    banks = Cat_bancos.query.all()
    json_data = []
    for bank in banks:
        r = {
            "nombre": bank.nombre,
            "fecha_registro": bank.fecha_registro,
            "activo": bank.activo,
        }
        json_data.append(r)
    return jsonify({"banks": json_data})


@app.route("/api/routes/<id>/")
def show_route_detail(id):
    coords = db.engine.execute("EXEC Cargar_Mapas_GPS " + id + ",'2017-06-27',1")
    json_data = []
    for coord in coords:
        c = {
            "lat": float(coord.latitud),
            "lng": float(coord.longitud),
        }
        json_data.append(c)

    return jsonify({"routes": json_data})


@app.route("/api/rutas")
def mostrar_rutas():
    rutas = db.engine.execute("SELECT id_ruta, nombre FROM cat_rutas WHERE activo = 1")
    json_data = []
    for ruta in rutas:
        c = {
            "id": ruta.id_ruta,
            "nombre": ruta.nombre,
        }
        json_data.append(c)

    return jsonify({"rutas": json_data})


if __name__ == "__main__":
    app.run(debug=True)
