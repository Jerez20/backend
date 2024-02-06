#Todas los prodcutos vendidos  por rango de fecha
#SELECT producto, (select descrip from producto where producto=a.producto)  descrip, sum (cantidad * -1) Cantidad FROM tradetalle a WHERE FECHA BETWEEN '20231218' AND '20231229' and tipo in ('03','04') group by producto

from flask import Flask, jsonify, request
import pyodbc
from datetime import datetime

app = Flask(__name__)

# Configuración de la conexión a la base de datos SQL Server
connection_string = 'DRIVER={SQL Server};SERVER=192.168.0.107,1433;DATABASE=PendaAsesys;UID=Sistema;PWD=@@sistema'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

@app.route('/productos', methods=['GET'])
def get_productos():
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
        query = """
            SELECT producto,
(SELECT descrip FROM producto WHERE producto = a.producto) AS descrip,
                   SUM(cantidad * -1) AS Cantidad
            FROM tradetalle a
            WHERE FECHA BETWEEN ? AND ? AND tipo IN ('03', '04')
            GROUP BY producto
        """
        cursor.execute(query, start_date, end_date)
        results = cursor.fetchall()

        # Crear una lista de resultados
        productos = []
        for row in results:
            producto = {
                'producto': row[0],
                'descrip': row[1],
                'cantidad': row[2]
            }
            productos.append(producto)

        return jsonify({'productos': productos})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
