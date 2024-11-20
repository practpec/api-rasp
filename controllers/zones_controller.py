from models.monitoring_model import verify_monitoring_exists, create_monitoring
from models.zones_model import verify_zone_exists, create_zone
from sensor.sensor_reader import read_sensor_data
from models.reads_model import insert_reads, calculate_averages
from models.result_zone_model import insert_result_zone
import time

def handle_zone_action(message):
    try:
        monitoring_id = message["monitoring_id"]
        projects_id = message["projects_id"]
        technical_managers_id = message["technical_managers_id"]
        status = message["status"]

        if not verify_monitoring_exists(monitoring_id):
            print(f"Monitoreo {monitoring_id} no existe. Creando monitoreo...")
            create_monitoring(monitoring_id, projects_id, technical_managers_id, status)
        else:
            print(f"Monitoreo {monitoring_id} ya existe.")

        zones_id = message["id_zone"]
        if not verify_zone_exists(zones_id):
            print(f"Zona {zones_id} no existe. Creando zona...")
            create_zone(zones_id, monitoring_id)
        else:
            print(f"Zona {zones_id} ya existe.")

        
        start_time = time.time()
        while time.time() - start_time < 180:
            data = read_sensor_data()
            if data:
                humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium = data
                insert_reads(zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium)
            else:
                print("No se obtuvieron datos del sensor para procesar.")
            time.sleep(15)
        
        print(f"Datos de la zona {zones_id} procesados e insertados con éxito.") 
        
        averages = calculate_averages(zones_id)
        if averages:
            insert_result_zone(zones_id, averages)
        else:
            print(f"No se pudo calcular e insertar promedios para la zona {zones_id}.")

                          
    except KeyError as e:
        print(f"Error en los datos del mensaje: falta el campo {e}.")
    except Exception as e:
        print(f"Error al procesar la acción por-zona: {e}")
