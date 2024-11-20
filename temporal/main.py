import paho.mqtt.client as mqtt
import json
import threading
import time

# Configuración del broker MQTT
MQTT_BROKER = '44.196.50.196'
MQTT_PORT = 1883
MQTT_USERNAME = 'guest'
MQTT_PASSWORD = 'guest'

# Topics de MQTT
RECEIVE_TOPIC = 'node-rasp'  # Topic para recibir mensajes
SEND_TOPIC = 'rasp-node'     # Topic para enviar mensajes


# Función que se ejecuta cuando el cliente se conecta al broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conexión exitosa al broker MQTT.")
        # Suscribirse al topic para recibir mensajes
        client.subscribe(RECEIVE_TOPIC)
        print(f"Suscrito al topic: {RECEIVE_TOPIC}")
    else:
        print(f"Error en la conexión: Código {rc}")


# Función que se ejecuta cuando se recibe un mensaje en el topic suscrito
def on_message(client, userdata, msg):
    try:
        # Intentar decodificar el mensaje como JSON
        message = msg.payload.decode('utf-8')
        try:
            json_message = json.loads(message)
            print(f"Mensaje recibido en {msg.topic}: {json_message}")

            # Procesa el mensaje de acuerdo a su contenido
            process_message(json_message, client)

        except json.JSONDecodeError:
            # Si no es JSON, tratarlo como texto
            print(f"Mensaje recibido (texto) en {msg.topic}: {message}")

    except Exception as e:
        print(f"Error al procesar mensaje en {msg.topic}: {e}")


# Función que procesa el mensaje de acuerdo a su contenido
def process_message(message, client):
    # Ejemplo: Si el mensaje contiene una clave específica, realiza una acción
    if "action" in message:
        action = message["action"]
        if action == "ping":
            response = {"response": "pong", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
        elif action == "status":
            response = {"response": "operational", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
        else:
            response = {"error": "Acción desconocida", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
    else:
        # Mensaje genérico
        response = {"error": "Mensaje no contiene una acción válida", "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}

    # Publicar la respuesta en el topic de envío
    client.publish(SEND_TOPIC, json.dumps(response))
    print(f"Respuesta enviada a {SEND_TOPIC}: {response}")


# Configuración del cliente MQTT
client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker y configurar la suscripción/publicación
try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Mantener el cliente en bucle para escuchar mensajes
    client.loop_forever()

except Exception as e:
    print(f"Error al conectar con el broker MQTT: {e}")
