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
