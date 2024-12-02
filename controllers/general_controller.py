from services.general.crops_service import compare_crops
from services.general.details_service import details
from models.data_model import calculate_averages
from models.general_model import insert_result
from mqtt.publisher import send_message

import sqlite3
import json


def handle_general_action(message):
    try:
        id_analysis = message["id_analysis"]
        averages = calculate_averages(id_analysis)
        insert_result(id_analysis, averages)
        compare_crops(id_analysis, averages)
        details(id_analysis, averages)
        message = data_analysis(id_analysis)
        
        send_message(message)

    except KeyError as e:
        print(f"Error en los datos del mensaje: falta el campo {e}.")
    except Exception as e:
        print(f"Error al procesar la acción general: {e}")



def data_analysis(id_analysis):
    db_path = 'database/terra-test.db'
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data_analysis WHERE id_analysis = ?", (id_analysis,))
        data_rows = cursor.fetchall()
        cursor.execute("SELECT * FROM resultados_analysis WHERE id_analysis = ?", (id_analysis,))
        promedio_rows = cursor.fetchall()
        result = {
            'data_analysis': data_rows,
            'resultados_analysis': promedio_rows
        }
        print("Se consulto la base de datos Generales")
        conn.close()
        return json.dumps(result, ensure_ascii=False)

    except Exception as e:
        print(f"Error al consultar la base de datos: {e}")
        return 'error'
  
