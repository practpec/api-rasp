import hashlib
import sqlite3
import time

def generate_unique_id(zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium):
    unique_string = f"{zones_id}{humidity}{temperature}{conductivity}{ph}{nitrogen}{phosphorus}{potassium}{time.time()}"
    
    unique_id = hashlib.sha256(unique_string.encode('utf-8')).hexdigest()[:64]
    
    return unique_id

def verify_reads_id_exists(unique_id):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM reads WHERE id=?", (unique_id,))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except sqlite3.Error as e:
        print(f"Error al verificar si el ID existe: {e}")
        return False

def insert_reads(zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium):
    try:
        unique_id = generate_unique_id(zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium)
        
        while verify_reads_id_exists(unique_id):
            print(f"El ID {unique_id} ya existe, generando uno nuevo.")
            unique_id = generate_unique_id(zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium)
        
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO reads 
                          (id, zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (unique_id, zones_id, humidity, temperature, conductivity, ph, nitrogen, phosphorus, potassium))
        conn.commit()
        conn.close()
        print(f"Resultado para zona {zones_id} insertado con éxito con ID {unique_id}.")
    
    except sqlite3.Error as e:
        print(f"Error al insertar resultados de la zona en la base de datos: {e}")
