
import threading

class SensorManager:
    def __init__(self):
        self.sensors_status = {}
        self.lock = threading.Semaphore(1)

    def add_sensor(self, sensor_id):
        
        with self.lock: 
            if sensor_id not in self.sensors_status:
                self.sensors_status[sensor_id] = "disponible"
                print(f"Sensor {sensor_id} agregado y marcado como disponible.")
            else:
                print(f"Sensor {sensor_id} ya existe.")

    def get_available_sensor(self):
      
        with self.lock:
            for sensor_id, status in self.sensors_status.items():
                if status == "disponible":
                    return sensor_id
        return None

    def lock_sensor(self, sensor_id):
       
        with self.lock:
            if sensor_id in self.sensors_status and self.sensors_status[sensor_id] == "disponible":
                self.sensors_status[sensor_id] = "ocupado"
                print(f"Sensor {sensor_id} bloqueado y marcado como ocupado.")
            else:
                print(f"Sensor {sensor_id} no disponible para bloquear.")

    def unlock_sensor(self, sensor_id):

        with self.lock:
            if sensor_id in self.sensors_status and self.sensors_status[sensor_id] == "ocupado":
                self.sensors_status[sensor_id] = "disponible"
                print(f"Sensor {sensor_id} desbloqueado y marcado como disponible.")
            else:
                print(f"Sensor {sensor_id} no estaba bloqueado.")
