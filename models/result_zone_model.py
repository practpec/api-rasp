import sqlite3

def verify_result_zone_id_exists(unique_id):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM result_zone WHERE id=?")
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except sqlite3.Error as e:
        print(f"Error al verificar si el ID existe: {e}")
        return False

def insert_result_zone(zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium):
    try:
        
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO result_zone 
                          (id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium))
        conn.commit()
        conn.close()
        
    
    except sqlite3.Error as e:
        print(f"Error al insertar resultados de la zona en la base de datos: {e}")
