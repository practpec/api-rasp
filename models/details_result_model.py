import sqlite3
from datetime import datetime

def insert_details_result(results_id, details):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        id_details = str(datetime.now().timestamp())

        cursor.execute('''
        INSERT INTO details_result (id, requeriments, results_id)
        VALUES (?, ?, ?);
        ''', (id_details, details, results_id))


        conn.commit()
        print(f"Detalles insertados correctamente para la zona {results_id}.")

    except sqlite3.Error as e:
        print(f"Error al insertar los detalles en la base de datos: {e}")
    
    finally:
        if conn:
            conn.close()


