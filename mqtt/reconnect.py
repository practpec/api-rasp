import time
from config import mqtt_config


def reconnect(client):
    max_retries = 100
    retry_delay = 5

    attempt = 0
    while attempt < max_retries:
        try:
            print(f"Intentando conectar al broker MQTT (Intento {attempt + 1}/{max_retries})...")
            client.connect(mqtt_config.MQTT_BROKER, mqtt_config.MQTT_PORT, 60)
            print("Conexion establecida")
            try:
                client.loop_forever()
            except KeyboardInterrupt:
                print("\nInterrupcion detectada. Cerrando conexion MQTT...")
                client.disconnect()
                break  

        except Exception as e:
            print(f"Error al conectar al broker MQTT: {e}")
            attempt += 1
            time.sleep(retry_delay)

    if attempt == max_retries:
        print("No se pudo establecer conexion. Finalizando cliente MQTT.")