import paho.mqtt.client as mqtt
import json
import time
from config import mqtt_config
from controllers.zones_controller import handle_zone_action

# Función que se ejecuta cuando el cliente se conecta al broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conexión exitosa al broker MQTT.")
        client.subscribe(mqtt_config.RECEIVE_TOPIC)
    else:
        print(f"Error en la conexión: Código {rc}")

# Función que se ejecuta cuando se recibe un mensaje en el topic suscrito
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

    else:
        print("Acción no reconocida.")

# Configuración del cliente MQTT
def start_mqtt_client():
    client = mqtt.Client()
    client.username_pw_set(mqtt_config.MQTT_USERNAME, mqtt_config.MQTT_PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(mqtt_config.MQTT_BROKER, mqtt_config.MQTT_PORT, 60)
    client.loop_forever()
