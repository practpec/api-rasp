import sqlite3

def verify_monitoring_exists(monitoring_id):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM monitoring WHERE id=?", (monitoring_id,))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except sqlite3.Error as e:
        print(f"Error al verificar monitoreo en la base de datos: {e}")
        return False

def create_monitoring(monitoring_id, projects_id, technical_managers_id, status):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO monitoring (id, projects_id, technical_managers_id, status) 
                          VALUES (?, ?, ?, ?)''', 
                       (monitoring_id, projects_id, technical_managers_id, status))
        conn.commit()
        conn.close()
        print(f"Monitoreo {monitoring_id} creado con éxito.")
    except sqlite3.Error as e:
        print(f"Error al crear monitoreo en la base de datos: {e}")
