#!flask/bin/python
from flask import Flask
from predecir import predecir 

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>San Francisco Forecast</h1></br><a href='http://127.0.0.1:5000/24'>Predicción de mañana</a></br><a href='http://127.0.0.1:5000/48'>Predicción de pasado mañana</a></br><a href='http://127.0.0.1:5000/72'>Predicción de 3 días</a>",200

@app.route('/24')
def vc():
    salida = predecir(24)
    return salida.to_html(),200

@app.route('/48')
def co():
    salida = predecir(48)
    return salida.to_html(),200

@app.route('/72')
def sd():
    salida = predecir(72)
    return salida.to_html(),200

if __name__ == '__main__':
    app.run(debug=True)