import time
from sensor.sensor_reader import read_sensor_data
from models.reads_model import insert_reads
import sqlite3

def collect_sensor_data(zones_id, duration=180, interval=15, stop_event=None):
    start_time = time.time()
    
    conn = sqlite3.connect('database/terra-test.db')
    
    try:
        conn.execute('BEGIN TRANSACTION')
        
        while time.time() - start_time < duration:
            if stop_event and stop_event.is_set():
                break

            data = read_sensor_data()
            if data:
                humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium = data
                insert_reads(zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium)
            else:
                print("No se obtuvieron datos del sensor para procesar.")
                if stop_event:
                    stop_event.set()
                break 
            time.sleep(interval)
        
        conn.commit()
    
    except Exception as e:
        conn.rollback()
        print(f"Error al recolectar datos para la zona {zones_id}: {e}")
    
    finally:
        conn.close()
    
    print(f"Recolección de datos para la zona {zones_id} terminada.")
