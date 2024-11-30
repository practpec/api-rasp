import json
import paho.mqtt.client as mqtt
from config import mqtt_config

def send_message(message):
    try:
        client = mqtt.Client()
        client.username_pw_set(mqtt_config.MQTT_USERNAME, mqtt_config.MQTT_PASSWORD)
        client.connect(mqtt_config.MQTT_BROKER, mqtt_config.MQTT_PORT, 60)

        if isinstance(message, dict):
            message = json.dumps(message)
        
        topic = mqtt_config.SEND_TOPIC
        client.publish(topic, message)
        print(f"Mensaje enviado al tema '{topic}': {message}")
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")
    finally:
        client.disconnect()
