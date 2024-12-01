from models.zones_model import verify_zone_exists, create_zone
import sqlite3

def ensure_zone_exists(zones_id, monitoring_id):
    conn = None
    try:
        conn = sqlite3.connect('database/terra-test.db')
        conn.execute('BEGIN TRANSACTION')

        if not verify_zone_exists(zones_id):
            print(f"Zona {zones_id} no existe. Creando zona...")
            create_zone(zones_id, monitoring_id)
        else:
            print(f"Zona {zones_id} ya existe.")
        
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"Error en la creación o verificación de la zona: {e}")
    finally:
        if conn:
            conn.close()
