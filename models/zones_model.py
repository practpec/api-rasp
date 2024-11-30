import sqlite3

def verify_zone_exists(zone_id):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM zones WHERE id=?", (zone_id,))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except sqlite3.Error as e:
        print(f"Error al verificar zona en la base de datos: {e}")
        return False

def create_zone(zone_id, monitoring_id):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO zones (id, monitoring_id) VALUES (?, ?)''',
                       (zone_id, monitoring_id))
        conn.commit()
        conn.close()
        print(f"Zona {zone_id} creada con éxito.")
    except sqlite3.Error as e:
        print(f"Error al crear zona en la base de datos: {e}")
