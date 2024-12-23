import json
import threading
from controllers.zones_controller import handle_zone_action
from controllers.general_controller import handle_general_action
from config import mqtt_config
import signal

stop_event = threading.Event()

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
    action = message.get("command")
    #por zona
    if action == "ejecutar_comandos.sh":
        zone_thread = threading.Thread(target=handle_zone_action, args=(message, stop_event))
        zone_thread.daemon = True
        zone_thread.start()
   #general
    elif action == "ejecutar_general.sh":
        general_thread = threading.Thread(target=handle_general_action, args=(message,))
        general_thread.daemon = True
        general_thread.start()

    else:
        print("Acción no reconocida.")

def signal_handler(sig, frame):
    print("\nInterrupción detectada. Cerrando todos los hilos...")
    stop_event.set()

signal.signal(signal.SIGINT, signal_handler)
