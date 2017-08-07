from flask import Flask, render_template, json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,)
