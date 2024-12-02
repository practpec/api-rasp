from models.monitoring_model import verify_monitoring_exists, create_monitoring
im
import sqlite3

def ensure_monitoring_exists(monitoring_id, projects_id, technical_managers_id, status):
    conn = None
    try:
        conn = sqlite3.connect('database/terra-test.db')
        conn.execute('BEGIN TRANSACTION')

        if not verify_monitoring_exists(monitoring_id):
            print(f"Monitoreo {monitoring_id} no existe. Creando monitoreo...")
            create_monitoring(monitoring_id, projects_id, technical_managers_id, status)
        else:
            print(f"Monitoreo {monitoring_id} ya existe.")

        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"Error en la creación o verificación del monitoreo: {e}")
    finally:
        if conn:
            conn.close()
