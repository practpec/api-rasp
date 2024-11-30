from mqtt.mqtt_client import start_mqtt_client

if __name__ == "__main__":
    try:
        start_mqtt_client()
    except KeyboardInterrupt:
        print("\nCerrando conexion MQTT...")
    except Exception as e:
        print(f"Error inesperado: {e}")
