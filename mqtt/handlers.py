import json
from controllers.zones_controller import handle_zone_action
from controllers.general_controller import handle_general_action
from config import mqtt_config

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conexión exitosa al broker MQTT")
        client.subscribe(mqtt_config.RECEIVE_TOPIC)
    else:
        print(f"Error en la conexión: Código {rc}")

def on_message(client, userdata, msg):
    message = msg.payload.decode('utf-8')
    try:
        json_message = json.loads(message)
        print(f"Mensaje recibido: {json_message}")
        process_message(json_message)
    except json.JSONDecodeError:
        print(f"Mensaje recibido (texto): {message}")
    except Exception as e:
        print(f"Error al procesar mensaje: {e}")

def process_message(message):
    action = message.get("action")
    if action == "por-zona":
        handle_zone_action(message)
    elif action == "general":
        handle_general_action(message)
    else:
        print("Acción no reconocida.")
