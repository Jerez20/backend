import pyodbc
from datetime import datetime
from flask import jsonify, request

# Configuración de la conexión a la base de datos SQL Server
connection_string = 'DRIVER={SQL Server};SERVER=192.168.0.107,1433;DATABASE=PendaAsesys;UID=Sistema;PWD=@@sistema'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

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

# Definir las otras funciones de consulta de la base de datos aquí...
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
        query = "SELECT COUNT(*) FROM TRANSA01 WHERE FECHA BETWEEN ? AND ?"
        cursor.execute(query, start_date, end_date)
        count = cursor.fetchone()[0]

        return jsonify({'count': count})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    ######################################################################
    
def get_transa_count_contado():
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
        query = "SELECT COUNT(*) FROM TRANSA01 WHERE FECHA BETWEEN ? AND ? AND TIPO = '03'"
        cursor.execute(query, start_date, end_date)
        count = cursor.fetchone()[0]

        return jsonify({'count': count})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    #####################################################################
def get_transa_count_credito():
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
    #########################################################################
    
def get_transa_sum_total_ventas():
    try:
        # Consultar el monto total de ventas realizadas por fecha
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
    ############################################################
def get_transa_sum_total_ventas_contado():
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
        query = "SELECT SUM(isnull(GRAVA,0)) GRAVADO, SUM(isnull(NOGRAVA,0)) NOGRABADO, SUM(isnull(ITBIS,0)) ITBIS, SUM(isnull(PROPINA,0)) PROPINA, SUM(isnull(MONTO,0)) TOTAL FROM TRANSA01 WHERE FECHA BETWEEN ? AND ? AND TIPO = '03'"
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
    #########################################################################
def get_transa_sum_total_ventas_credito():
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
        query = "SELECT SUM(isnull(GRAVA,0)) GRAVADO, SUM(isnull(NOGRAVA,0)) NOGRABADO, SUM(isnull(ITBIS,0)) ITBIS, SUM(isnull(PROPINA,0)) PROPINA, SUM(isnull(MONTO,0)) TOTAL FROM TRANSA01 WHERE FECHA BETWEEN ? AND ? AND TIPO = '04'"
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
    ################################################################
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