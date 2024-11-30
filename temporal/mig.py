import sqlite3
import uuid

# Diccionario de cultivos
cultivos = {
    "Café": {
        "Humedad": (70, 90),
        "Temperatura": (18, 24),
        "Conductividad (EC)": (140, 2000),
        "pH": (6.0, 8.5),
        "Nitrógeno": (0, 200),
        "Fósforo": (0, 60),
        "Potasio": (0, 300)
    },
    "Cacao": {
        "Humedad": (70, 90),
        "Temperatura": (22, 30),
        "Conductividad (EC)": (200, 1500),
        "pH": (6.0, 7.0),
        "Nitrógeno": (50, 150),
        "Fósforo": (20, 50),
        "Potasio": (100, 200)
    },
    "Maí­z": {
        "Humedad": (40, 60),
        "Temperatura": (18, 30),
        "Conductividad (EC)": (100, 5000),
        "pH": (5.5, 7.0),
        "Nitrógeno": (30, 150),
        "Fósforo": (30, 60),
        "Potasio": (100, 300)
    },
    "Mango": {
        "Humedad": (50, 80),
        "Temperatura": (24, 30),
        "Conductividad (EC)": (300, 1500),
        "pH": (5.5, 7.5),
        "Nitrógeno": (20, 100),
        "Fósforo": (10, 40),
        "Potasio": (100, 250)
    },
    "Caña": {
        "Humedad": (70, 90),
        "Temperatura": (20, 30),
        "Conductividad (EC)": (100, 2000),
        "pH": (6.0, 7.5),
        "Nitrógeno": (50, 200),
        "Fósforo": (20, 60),
        "Potasio": (100, 300)
    },
    "Plátano": {
        "Humedad": (60, 90),
        "Temperatura": (24, 30),
        "Conductividad (EC)": (500, 2000),
        "pH": (5.5, 7.0),
        "Nitrógeno": (50, 150),
        "Fósforo": (20, 60),
        "Potasio": (200, 400)
    },
    "Frijol": {
        "Humedad": (60, 70),
        "Temperatura": (20, 30),
        "Conductividad (EC)": (100, 5000),
        "pH": (6.0, 7.5),
        "Nitrógeno": (20, 60),
        "Fósforo": (50, 150),
        "Potasio": (100, 200)
    },
    "Cacahuate": {
        "Humedad": (50, 70),
        "Temperatura": (21, 30),
        "Conductividad (EC)": (100, 5000),
        "pH": (5.8, 6.5),
        "Nitrógeno": (20, 50),
        "Fósforo": (50, 150),
        "Potasio": (150, 300)
    },
    "Calabaza": {
        "Humedad": (60, 80),
        "Temperatura": (20, 25),
        "Conductividad (EC)": (100, 2500),
        "pH": (6.0, 7.0),
        "Nitrógeno": (30, 80),
        "Fósforo": (50, 150),
        "Potasio": (100, 200)
    },
    "Cebolla": {
        "Humedad": (50, 70),
        "Temperatura": (12, 24),
        "Conductividad (EC)": (100, 5000),
        "pH": (6.0, 7.0),
        "Nitrógeno": (30, 80),
        "Fósforo": (50, 150),
        "Potasio": (100, 200)
    },
    "Aguacate": {
        "Humedad": (60, 80),
        "Temperatura": (16, 26),
        "Conductividad (EC)": (500, 1500),
        "pH": (5.5, 7.0),
        "Nitrógeno": (50, 150),
        "Fósforo": (20, 60),
        "Potasio": (100, 300)
    }
}
def insert_crops_data(cultivos):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        
        for crop, data in cultivos.items():
            humidity_min, humidity_max = data["Humedad"]
            temperature_min, temperature_max = data["Temperatura"]
            conductivity_min, conductivity_max = data["Conductividad (EC)"]
            ph_min, ph_max = data["pH"]
            nitrogen_min, nitrogen_max = data["Nitrógeno"]
            phosphorus_min, phosphorus_max = data["Fósforo"]
            potassium_min, potassium_max = data["Potasio"]
            
            # Generar un ID único
            crop_id = str(uuid.uuid4())
            
            # Insertar en la tabla
            cursor.execute('''
                INSERT INTO crops (
                    id, crop, humidity_min, humidity_max, temperature_min, temperature_max,
                    conductivity_min, conductivity_max, ph_min, ph_max, nitrogen_min, nitrogen_max,
                    phosphorus_min, phosphorus_max, potassium_min, potassium_max
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                crop_id, crop, humidity_min, humidity_max, temperature_min, temperature_max,
                conductivity_min, conductivity_max, ph_min, ph_max, nitrogen_min, nitrogen_max,
                phosphorus_min, phosphorus_max, potassium_min, potassium_max
            ))
        
        conn.commit()
        conn.close()
        print("Datos de cultivos insertados exitosamente.")
    
    except sqlite3.Error as e:
        print(f"Error al insertar datos de cultivos: {e}")

# Llamar a la función
insert_crops_data(cultivos)
