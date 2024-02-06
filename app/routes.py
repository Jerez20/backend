from flask import jsonify, request
from flask import Flask
from database import get_transa_data, get_transa_count, get_transa_count_contado, \
    get_transa_count_credito, get_transa_sum_total_ventas, get_transa_sum_total_ventas_contado, \
    get_transa_sum_total_ventas_credito, get_productos


app = Flask(__name__)
# Definir las rutas aquí
@app.route('/transa', methods=['GET'])
def transa():
    return get_transa_data()

@app.route('/transa/count', methods=['GET'])
def transa_count():
    return get_transa_count()

@app.route('/transa/count/contado', methods=['GET'])
def transa_count_contado():
    return get_transa_count_contado()

@app.route('/transa/count/credito', methods=['GET'])
def transa_count_credito():
    return get_transa_count_credito()

@app.route('/transa/sum/total/ventas', methods=['GET'])
def transa_sum_total_ventas():
    return get_transa_sum_total_ventas()

@app.route('/transa/sum/total/ventas/contado', methods=['GET'])
def transa_sum_total_ventas_contado():
    return get_transa_sum_total_ventas_contado()

@app.route('/transa/sum/total/ventas/credito', methods=['GET'])
def transa_sum_total_ventas_credito():
    return get_transa_sum_total_ventas_credito()

@app.route('/productos', methods=['GET'])
def productos():
    return get_productos()
