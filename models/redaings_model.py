import sqlite3

def insert_reads(id_analysis, id_zone, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium):
    conn = None
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        
        conn.execute('BEGIN TRANSACTION')
        
        cursor.execute('''INSERT INTO readings 
                          (id_analysis, id_zone, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (id_analysis, id_zone, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium))
        
        conn.commit()
        print(f"Lectura insertada con éxito para la zona {id_zone}.")
    
    except sqlite3.Error as e:
        if conn:
            conn.rollback() 
        print(f"Error al insertar resultados de la zona en la base de datos: {e}")
    
    finally:
        if conn:
            conn.close()
            
def calculate_averages(id_zone):
    
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT 
                AVG(humidity) as avg_humidity,
                AVG(temperature) as avg_temperature,
                AVG(conductivity) as avg_conductivity,
                AVG(ph) as avg_ph,
                AVG(nitrogen) as avg_nitrogen,
                AVG(phosphorus) as avg_phosphorus,
                AVG(potassium) as avg_potassium
            FROM readings
            WHERE id_zone = ?
        ''', (id_zone,))
        
        averages = cursor.fetchone() 
        conn.close()

        if averages:
            return {
                "humidity": averages[0],
                "temperature": averages[1],
                "conductivity": averages[2],
                "ph": averages[3],
                "nitrogen": averages[4],
                "phosphorus": averages[5],
                "potassium": averages[6]
            }
        else:
            print(f"No se encontraron lecturas para calcular promedios de la zona {id_zone}.")
            return None

    except sqlite3.Error as e:
        print(f"Error al calcular promedios: {e}")
        return None

