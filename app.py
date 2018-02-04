from flask import Flask, render_template, json, jsonify
from flask_sqlalchemy import SQLAlchemy
import urllib
import urllib.parse

app = Flask(__name__)
params = urllib.parse.quote_plus(
#    "DRIVER={SQL SERVER};SERVER=DESKTOP-43GJF30;DATABASE=dsd_mazatlan;UID=sa;PWD=Dsdsistemas2012")
       "DRIVER={SQL SERVER};SERVER=localhost;DATABASE=dsd_mazatlan;UID=sa;PWD=Dsdsistemas2012")
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/vue")
def vue():
    return render_template("vue_example.html")


@app.route("/vue_v2")
def vue_v2():
    return render_template("vue_example_2.html")


@app.route("/bind")
def bind():
    return render_template("v-bind.html")


@app.route("/ajax")
def ajax():
    return render_template("ajax.html")


@app.route("/show")
def show():
    return render_template("v-show.html")


@app.route("/template")
def template():
    return render_template("template.html")


@app.route("/eventos")
def eventos():
    return render_template("eventos.html")


@app.route("/filtros")
def filtros():
    return render_template("filtros.html")


@app.route("/recorrido")
def recorrido():
    return render_template("recorrido.html")


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
def show_routes():
    query = """SELECT 
                hu.id_ruta, hu.kilometrage_dia, rut.ruta 
                FROM historial_ubicaciones hu
                INNER JOIN cat_rutas rut ON rut.id_ruta = hu.id_ruta 
                WHERE hu.fecha_registro = '2017-01-27' AND rut.activo = 1
                ORDER BY rut.nombre"""

    rutas = db.engine.execute(query)
    json_data = []
    for ruta in rutas:
        c = {
            "id": ruta.id_ruta,
            "route": ruta.ruta,
            "kilometers": ruta.kilometrage_dia,
        }
        json_data.append(c)
    return jsonify(json_data)

@app.route("/gps")
def show_points_gps():
    query = "EXEC Cargar_Mapas_GPS 19,'2017-08-05',1"

    points_gps = db.engine.execute(query)
    json_points_gps = []
    for point in points_gps:
        c = {
            "no": point.No,
            "hour": point.hora,
            "lat": point.latitud,
            "long": point.longitud,
            "speed": point.velocidad,
        }
        json_points_gps.append(c)
    return jsonify(json_points_gps)


@app.route("/visitas")
def show_visits():
    query = "EXEC Rep_Recorrido 2, 7,'2017-08-01',''"

    visits = db.engine.execute(query)
    json_visits = []
    for visit in visits:
        c = {
            "id_route": visit.id_ruta,
            "id_client": visit.id_cliente,
            "client_name": visit.establecimiento,
            "order": visit.orden,
            "hour_begin": visit.hora_inicio,
            "hour_finish": visit.hora_fin,
            "sale_total": visit.venta,
            "outside_route": visit.programados,
            "visit_it": visit.justificacion,
        }
        json_visits.append(c)
    return jsonify(json_visits)


@app.route("/clientes")
def show_clients():
    query = """SELECT
                dtv.id_ruta, dtv.id_cliente, dtv.orden, 
                cli.establecimiento, dtv.latitud, dtv.longitud 
                FROM cat_clientes_datos_venta dtv
                INNER JOIN cat_clientes cli ON cli.id_cliente = dtv.id_cliente AND cli.activo = 1
                WHERE dia = DATEPART(DW, '2017-08-04') AND fecha_baja IS NULL AND dtv.id_ruta = 19
                GROUP BY dtv.id_cliente, dtv.id_ruta, dtv.id_cliente, cli.establecimiento, dtv.orden, dtv.latitud, dtv.longitud
                ORDER BY dtv.orden"""

    clients = db.engine.execute(query)
    json_clients = []
    for client in clients:
        c = {
            "id": client.id_cliente,
            "order": client.orden,
            "name": client.establecimiento,
            "lat": client.latitud,
            "long": client.longitud,
        }
        json_clients.append(c)
    return jsonify(json_clients)


@app.route("/cedis")
def mostrar_cedis():
    cat_cedis = db.engine.execute("SELECT id_cedis, nombre FROM cat_cedis WHERE activo = 1 ORDER BY orden")
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
    app.run(host='0.0.0.0', debug=True, port=5000)
