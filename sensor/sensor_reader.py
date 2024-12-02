import minimalmodbus
import serial

#windows
instrument = minimalmodbus.Instrument('COM6', 1)

#linux
#instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) 

instrument.serial.baudrate = 4800
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.5

def read_sensor_data():
    try:

        humidity = instrument.read_register(1, 1, functioncode=3) * 0.1  # Humedad
        temperature = instrument.read_register(2, 1, functioncode=3) * 0.1  # Temperatura
        conductivity = instrument.read_register(3, 1, functioncode=3)  # Conductividad
        ph = instrument.read_register(4, 1, functioncode=3) * 0.1  # pH
        nitrogen = instrument.read_register(5, 1, functioncode=3)  # Nitrógeno
        phosphorus = instrument.read_register(6, 1, functioncode=3)  # Fósforo
        potassium = instrument.read_register(7, 1, functioncode=3)  # Potasio
        
        return humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium
    
    except minimalmodbus.NoResponseError as e:
        print(f"Error de lectura: No se recibió respuesta del sensor. {str(e)}")
    except minimalmodbus.InvalidResponseError as e:
        print(f"Error de lectura: Respuesta inválida del sensor. {str(e)}")
    except serial.SerialException as e:
        print(f"Error de comunicación con el sensor: {str(e)}")
    except Exception as e:
        print(f"Error de lectura: {str(e)}")
    return None

read_sensor_data()
