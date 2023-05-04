from flask import Flask, jsonify
import json

app = Flask(__name__)
with open('generated.json') as file:
    datos = json.load(file)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/datos')
def datos():
    return jsonify(datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)