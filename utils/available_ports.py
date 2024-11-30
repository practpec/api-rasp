import pyudev
from mqtt.publisher import send_message

def list_connected_devices():
    context = pyudev.Context()
    usb_devices = [
        device for device in context.list_devices(subsystem='tty')
        if device.get('ID_VENDOR') and device.get('ID_MODEL')
        and ('USB' in device.get('ID_MODEL', '') or 'ACM' in device.get('ID_MODEL', ''))
    ]
    return usb_devices

def notify_sensor_count(sensor_count):
    message = {
        "action": "sensor-count",
        "sensor_count": sensor_count
    }
    send_message(message)

def monitor_device_changes():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='tty')
    monitor.start()

    print("Monitoreando cambios en los dispositivos...")

    usb_devices = list_connected_devices()
    initial_count = len(usb_devices)
    print(f"Cantidad inicial de sensores: {initial_count}")
    notify_sensor_count(initial_count)

    previous_count = initial_count

    try:
        while True:
            device = monitor.poll()
            if device:
                usb_devices = list_connected_devices()
                current_count = len(usb_devices)

                if current_count != previous_count:
                    print(f"Se ha detectado un cambio en la cantidad de sensores. Total: {current_count}")
                    notify_sensor_count(current_count)
                    previous_count = current_count
    except KeyboardInterrupt:
        print("\nMonitoreo detenido por el usuario.")
