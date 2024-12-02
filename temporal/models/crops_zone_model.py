import sqlite3
import hashlib
import time

def generate_unique_id(data):
    unique_string = f"{data}{time.time()}"
    return hashlib.sha256(unique_string.encode('utf-8')).hexdigest()[:64]

def insert_crops_zone(zones_id, crops_zone):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        for crop in crops_zone:
            unique_id = generate_unique_id(f"{zones_id}{crop['crops_id']}")

            cursor.execute('''
            INSERT INTO crops_zone (id, suitable, crops_id, details, zones_id)
            VALUES (?, ?, ?, ?, ?)
            ''', (
                unique_id,
                crop['suitable'],
                crop['crops_id'],
                str(crop['details']),
                zones_id
            ))

        conn.commit()
        print(f"Se han insertado {len(crops_zone)} registros en crops_zone para la zona {zones_id}.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos en crops_zone: {e}")
    finally:
        conn.close()
