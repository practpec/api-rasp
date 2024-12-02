import sqlite3

def insert_result_zone(id_analysis, id_zone, averages):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()


        cursor.execute('''
            INSERT INTO data 
                (id_analysis, id_zone, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            id_analysis,
            id_zone,
            averages["humidity"],
            averages["temperature"],
            averages["conductivity"],
            averages["ph"],
            averages["nitrogen"],
            averages["phosphorus"],
            averages["potassium"]
        ))
        
        conn.commit()
        conn.close()

        print(f"Promedios insertados en result_zone con ID {id_zone}.")
    except sqlite3.Error as e:
        print(f"Error al insertar promedios en result_zone: {e}")
        
def calculate_averages(id_analysis):
    
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
            FROM data
            WHERE id_analysis = ?
        ''', (id_analysis,))
        
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
            print(f"No se encontraron lecturas para calcular promedios de la zona {id_analysis}.")
            return None

    except sqlite3.Error as e:
        print(f"Error al calcular promedios: {e}")
        return None