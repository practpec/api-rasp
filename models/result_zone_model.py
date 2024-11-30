import sqlite3

def insert_result_zone(zones_id, averages):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()


        cursor.execute('''
            INSERT INTO result_zone 
                (id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            zones_id,
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

        print(f"Promedios insertados en result_zone con ID {zones_id}.")
    except sqlite3.Error as e:
        print(f"Error al insertar promedios en result_zone: {e}")

def calculate_averages(monitoring_id):
    print(monitoring_id)
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id FROM zones WHERE monitoring_id = ?
        ''', (monitoring_id))
        
        zones_ids = cursor.fetchall()
        print(zones_ids)
        if not zones_ids:
            print(f"No se encontraron zonas para el monitoreo {monitoring_id}.")
            conn.close()
            return None

        sum_humidity = 0
        sum_temperature = 0
        sum_conductivity = 0
        sum_ph = 0
        sum_nitrogen = 0
        sum_phosphorus = 0
        sum_potassium = 0
        count = 0

        for zone_id in zones_ids:
            zone_id = zone_id[0] 
            cursor.execute('''
                SELECT 
                    humidity,
                    temperature,
                    conductivity,
                    ph,
                    nitrogen,
                    phosphorus,
                    potassium
                FROM result_zone
                WHERE zones_id = ?
            ''', (zone_id,))

            rows = cursor.fetchall()  
            for row in rows:
                sum_humidity += row[0]
                sum_temperature += row[1]
                sum_conductivity += row[2]
                sum_ph += row[3]
                sum_nitrogen += row[4]
                sum_phosphorus += row[5]
                sum_potassium += row[6]
                count += 1 

        conn.close()

        if count == 0:
            print(f"No se encontraron lecturas para calcular promedios en las zonas asociadas al monitoreo {monitoring_id}.")
            return None

        
        return {
            "humidity": sum_humidity / count,
            "temperature": sum_temperature / count,
            "conductivity": sum_conductivity / count,
            "ph": sum_ph / count,
            "nitrogen": sum_nitrogen / count,
            "phosphorus": sum_phosphorus / count,
            "potassium": sum_potassium / count,
        }
        
    except sqlite3.Error as e:
        print(f"Error al calcular promedios: {e}")
        return None

