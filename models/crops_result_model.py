import sqlite3
import hashlib
import time

def generate_unique_id(data):
    unique_string = f"{data}{time.time()}"
    return hashlib.sha256(unique_string.encode('utf-8')).hexdigest()[:64]

def insert_crops_result(result_id, crops_result):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        for crop in crops_result:
            unique_id = generate_unique_id(f"{result_id}{crop['crops_id']}")

            cursor.execute('''
            INSERT INTO crops_result (id, suitable, crops_id, details, results_id)
            VALUES (?, ?, ?, ?, ?)
            ''', (
                unique_id,
                crop['suitable'],
                crop['crops_id'],
                str(crop['details']),
                result_id
            ))

        conn.commit()
        print(f"Se han insertado {len(crops_result)} registros en crops_result para la zona {result_id}.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos en crops_result: {e}")
    finally:
        conn.close()
