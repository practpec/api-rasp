import sqlite3

def insert_result(id_analysis, averages):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO data_analysis 
                (id_analysis, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            id_analysis,
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

        print(f"Promedios insertados en general con ID {id_analysis}.")
    except sqlite3.Error as e:
        print(f"Error al insertar promedios en general: {e}")
     