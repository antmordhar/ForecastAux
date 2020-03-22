#!flask/bin/python
from flask import Flask
from sklearn.externals import joblib
from predecir import predecir 

app = Flask(__name__)
# modeloTemperatura= joblib.load('./Modelos/modeloTemperatura.pkl')
# modeloHumidity= joblib.load('./Modelos/modeloHumidity.pkl')
modeloTemperatura= joblib.load('/tmp/workflow/Forecast/Modelos/modeloTemperatura.pkl')
modeloHumidity= joblib.load('/tmp/workdflow/Forecast/Modelos/modeloHumidity.pkl')

@app.route('/')
def index():
    return "<h1>San Francisco Forecast</h1></br><a href='http://127.0.0.1:5000/24'>Predicción de mañana</a></br><a href='http://127.0.0.1:5000/48'>Predicción de pasado mañana</a></br><a href='http://127.0.0.1:5000/72'>Predicción de 3 días</a>"

@app.route('/24')
def vc():
    salida = predecir(24,modeloTemperatura,modeloHumidity).to_html()
    return salida

@app.route('/48')
def co():
    salida = predecir(48,modeloTemperatura,modeloHumidity).to_html()
    return salida

@app.route('/72')
def sd():
    salida = predecir(72,modeloTemperatura,modeloHumidity).to_html()
    return salida

if __name__ == '__main__':
    app.run(debug=True)