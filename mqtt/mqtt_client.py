import paho.mqtt.client as mqtt
from config import mqtt_config
from mqtt.handlers import on_connect, on_message
from mqtt.reconnect import reconnect

def start_mqtt_client():
    global mqtt_client
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(mqtt_config.MQTT_USERNAME, mqtt_config.MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    reconnect(mqtt_client)
   
