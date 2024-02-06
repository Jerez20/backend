#Conteo total de facturas de credito por rango de fecha
#SELECT COUNT(*) FROM TRANSA01 WHERE FECHA BETWEEN '20231218' AND '20231229' AND TIPO ='04'

from flask import Flask, jsonify, request
import pyodbc
from datetime import datetime

app = Flask(__name__)

# Configuración de la conexión a la base de datos SQL Server
connection_string = 'DRIVER={SQL Server};SERVER=192.168.0.107,1433;DATABASE=PendaAsesys;UID=Sistema;PWD=@@sistema'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

@app.route('/transa/count/credito', methods=['GET'])
def get_transa_count():
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
        query = "SELECT COUNT(*) FROM TRANSA01 WHERE FECHA BETWEEN ? AND ? AND TIPO = '04'"
        cursor.execute(query, start_date, end_date)
        count = cursor.fetchone()[0]

        return jsonify({'count': count})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
