import time
from sensor.sensor_reader import read_sensor_data
from models.reads_model import insert_reads

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
