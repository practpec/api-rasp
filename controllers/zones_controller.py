from services.zones.sensor_service import collect_sensor_data
from services.zones.data_processing_service import process_zone_averages, compare_crops
from services.zones.details_service import generate_zone_details
from models.redaings_model import calculate_averages
from mqtt.publisher import send_message
import sqlite3
import json

def handle_zone_action(message, stop_event):
    try:
        id_analysis = message["id_analysis"]
        id_zone = message["id_zone"]
        collect_sensor_data(id_analysis, id_zone, stop_event=stop_event)
        if stop_event and stop_event.is_set():
            return 

        averages = calculate_averages(id_zone)
        process_zone_averages(id_analysis, id_zone, averages)
        compare_crops(id_analysis, id_zone, averages)
        generate_zone_details(id_analysis, id_zone, averages)
        message = data_zone(id_analysis, id_zone)
    
        send_message(message)

    except KeyError as e:
        print(f"Error en los datos del mensaje: falta el campo {e}.")
    except Exception as e:
        print(f"Error al procesar la acción por zona: {e}")


def data_zone(id_analysis, id_zone):
    db_path = 'database/terra-test.db'
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data WHERE id_zone = ? AND id_analysis = ?", (id_zone, id_analysis,))
        data_rows = cursor.fetchall()
        cursor.execute("SELECT * FROM resultados_cultivos WHERE id_zone = ? AND id_analysis = ?", (id_zone, id_analysis,))
        promedio_rows = cursor.fetchall()
        
        result = {
            'data': data_rows,
            'resultados_cultivos': promedio_rows
        }
        print("Se consulto la base de datos por  zona")
        conn.close()
        return json.dumps(result, ensure_ascii=False)

    except Exception as e:
        print(f"Error al consultar la base de datos: {e}")
        return 'error'