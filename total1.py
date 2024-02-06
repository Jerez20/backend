#Total de ventas por rango de fecha
#SELECT  SUM(isnull(GRAVA,0)) GRAVADO, SUM(isnull(NOGRAVA,0)) NOGRABADO, SUM(isnull(ITBIS,0)) ITBIS, SUM(isnull(PROPINA,0)) PROPINA,SUM(isnull(MONTO,0)) TOTAL  FROM TRANSA01 WHERE FECHA BETWEEN '20231218' AND '20231229' 

from flask import Flask, jsonify, request
import pyodbc
from datetime import datetime

app = Flask(__name__)

# Configuración de la conexión a la base de datos SQL Server
connection_string = 'DRIVER={SQL Server};SERVER=192.168.0.107,1433;DATABASE=PendaAsesys;UID=Sistema;PWD=@@sistema'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

@app.route('/transa/sum/total/ventas', methods=['GET'])
def get_transa_sum():
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
        query = "SELECT SUM(isnull(GRAVA,0)) GRAVADO, SUM(isnull(NOGRAVA,0)) NOGRABADO, SUM(isnull(ITBIS,0)) ITBIS, SUM(isnull(PROPINA,0)) PROPINA, SUM(isnull(MONTO,0)) TOTAL FROM TRANSA01 WHERE FECHA BETWEEN ? AND ?"
        cursor.execute(query, start_date, end_date)
        result = cursor.fetchone()

        # Extraer los resultados
        gravado = result[0]
        nograbado = result[1]
        itbis = result[2]
        propina = result[3]
        total = result[4]

        return jsonify({'gravado': gravado, 'nogravado': nograbado, 'itbis': itbis, 'propina': propina, 'total': total})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
