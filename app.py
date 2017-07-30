from flask import Flask, json
app = Flask(__name__)


@app.route("/")
def index():
    return "hola desde index"


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
