import minimalmodbus
import serial
import time

instrument = minimalmodbus.Instrument('COM6', 1)

instrument.serial.baudrate = 4800  # Velocidad en baudios
instrument.serial.bytesize = 8     # Bits de datos
instrument.serial.parity = serial.PARITY_NONE  # Paridad
instrument.serial.stopbits = 1     # Bits de parada
instrument.serial.timeout = 0.5    # Tiempo de espera para la respuesta


def read_sensor_data():
    try:
        humidity = instrument.read_register(1, 1, functioncode=3) * 0.1  # Humedad
        temperature = instrument.read_register(2, 1, functioncode=3) * 0.1  # Temperatura
        conductivity = instrument.read_register(3, 1, functioncode=3)  # Conductividad
        ph = instrument.read_register(4, 1, functioncode=3) * 0.1  # pH
        nitrogen = instrument.read_register(5, 1, functioncode=3)  # Nitrógeno
        phosphorus = instrument.read_register(6, 1, functioncode=3)  # Fósforo
        potassium = instrument.read_register(7, 1, functioncode=3)  # Potasio

        print(f"Humedad: {humidity}%")
        print(f"Temperatura: {temperature}°C")
        print(f"Conductividad: {conductivity} µS/cm")
        print(f"pH: {ph}")
        print(f"Nitrógeno: {nitrogen} mg/kg")
        print(f"Fósforo: {phosphorus} mg/kg")
        print(f"Potasio: {potassium} mg/kg")

    except Exception as e:
        print(f"Error de lectura: {str(e)}")

start_time = time.time()
while time.time() - start_time < 180:
    read_sensor_data()
    time.sleep(15)