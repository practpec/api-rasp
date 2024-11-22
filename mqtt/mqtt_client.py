import paho.mqtt.client as mqtt
import time
import json

from config import mqtt_config
from controllers.zones_controller import handle_zone_action
from controllers.general_controller import handle_general_action


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conexión exitosa al broker MQTT \nEscuchando en: {mqtt_config.RECEIVE_TOPIC}")
        client.subscribe(mqtt_config.RECEIVE_TOPIC)
    else:
        print(f"Error en la conexión: Código {rc}")


def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    try:
        json_message = json.loads(message)
        print(f"Mensaje recibido: {json_message}")
        process_message(json_message, client)
    except json.JSONDecodeError:
        print(f"Mensaje recibido (texto): {message}")
    except Exception as e:
        print(f"Error al procesar mensaje: {e}")


def process_message(message, client):
    action = message.get("action")
    if action == "por-zona":
        handle_zone_action(message)
    elif action == "general":
        handle_general_action(message)
    else:
        print("Acción no reconocida.")


def start_mqtt_client():
    client = mqtt.Client()
    client.username_pw_set(mqtt_config.MQTT_USERNAME, mqtt_config.MQTT_PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message

    reconnect(client)


def reconnect(client):
    max_retries = 100
    retry_delay = 5

    attempt = 0
    while attempt < max_retries:
        try:
            print(f"Intentando conectar al broker MQTT (Intento {attempt + 1}/{max_retries})...")
            client.connect(mqtt_config.MQTT_BROKER, mqtt_config.MQTT_PORT, 60)
            print("Conexión establecida")
            client.loop_forever()
            break
        except Exception as e:
            print(f"Error al conectar al broker MQTT: {e}")
            attempt += 1
            time.sleep(retry_delay)

    if attempt == max_retries:
        print("No se pudo establecer conexión. Finalizando cliente MQTT.")
