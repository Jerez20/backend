#Todas las trasaccines de ventas por rango de fecha

from flask import Flask, jsonify, request
import pyodbc
from datetime import datetime

app = Flask(__name__)

# Configuración de la conexión a la base de datos SQL Server
connection_string = 'DRIVER={SQL Server};SERVER=192.168.0.107,1433;DATABASE=PendaAsesys;UID=Sistema;PWD=@@sistema'

conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

@app.route('/transa', methods=['GET'])
def get_transa_data():
    try:
        # Obtener parámetros de la solicitud
        start_date_str = request.args.get('start_date', '')
        end_date_str = request.args.get('end_date', '')

        # Verificar que se proporcionen ambas fechas
        if not start_date_str or not end_date_str:
            return jsonify({'error': 'Debes proporcionar las fechas de inicio y fin.'}), 400

        # Convertir las cadenas de fecha a objetos datetime
        start_date = datetime.strptime(start_date_str, '%Y%m%d')
        end_date = datetime.strptime(end_date_str, '%Y%m%d')

        # Realizar la consulta en la base de datos
        query = "SELECT * FROM TRANSA01 WHERE FECHA BETWEEN ? AND ?"
        results = []
        cursor.execute(query, start_date, end_date)
        columns = [column[0] for column in cursor.description]

        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))

        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
