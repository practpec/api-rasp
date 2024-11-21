from models.monitoring_model import verify_monitoring_exists, create_monitoring
from models.zones_model import verify_zone_exists, create_zone
from sensor.sensor_reader import read_sensor_data
from models.reads_model import insert_reads, calculate_averages
from models.result_zone_model import insert_result_zone
from models.crops_zone_model import insert_crops_zone
from models.details_zone_model import insert_details_zone

from helpers.compare_helper import check_crops
from helpers.details_helper import generate_details

import time

def ensure_monitoring_exists(monitoring_id, projects_id, technical_managers_id, status):
    if not verify_monitoring_exists(monitoring_id):
        print(f"Monitoreo {monitoring_id} no existe. Creando monitoreo...")
        create_monitoring(monitoring_id, projects_id, technical_managers_id, status)
    else:
        print(f"Monitoreo {monitoring_id} ya existe.")

def ensure_zone_exists(zones_id, monitoring_id):
    if not verify_zone_exists(zones_id):
        print(f"Zona {zones_id} no existe. Creando zona...")
        create_zone(zones_id, monitoring_id)
    else:
        print(f"Zona {zones_id} ya existe.")

def collect_sensor_data(zones_id, duration=180, interval=15):
    start_time = time.time()
    while time.time() - start_time < duration:
        data = read_sensor_data()
        if data:
            humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium = data
            insert_reads(zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium)
        else:
            print("No se obtuvieron datos del sensor para procesar.")
        time.sleep(interval)
    print(f"Datos de la zona {zones_id} procesados e insertados con éxito.")

def process_zone_averages(zones_id, averages):
   
    if averages:
        insert_result_zone(zones_id, averages)
    else:
        print(f"No se pudo calcular e insertar promedios para la zona {zones_id}.")

def compare_crops(zones_id, averages):
    if averages:
        crops_zone = check_crops(averages)
        insert_crops_zone(zones_id, crops_zone)
    else:
        print("No se pudo comprobar los cultivos")

def details(zones_id, averages):
    if averages:
        details =  generate_details(averages)
        insert_details_zone(zones_id, details)
    else:
        print("No se pudo generar los detalles de la zona")   

def handle_zone_action(message):
    try:
        monitoring_id = message["monitoring_id"]
        projects_id = message["projects_id"]
        technical_managers_id = message["technical_managers_id"]
        status = message["status"]
        zones_id = message["id_zone"]

        ensure_monitoring_exists(monitoring_id, projects_id, technical_managers_id, status)
        ensure_zone_exists(zones_id, monitoring_id)
        
        collect_sensor_data(zones_id)
        
        averages = calculate_averages(zones_id)
        
        #posible concurrencia
        process_zone_averages(zones_id, averages)
        compare_crops(zones_id, averages)
        details(zones_id, averages)

    except KeyError as e:
        print(f"Error en los datos del mensaje: falta el campo {e}.")
    except Exception as e:
        print(f"Error al procesar la acción por zona: {e}")
