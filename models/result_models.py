import sqlite3 
import hashlib
import uuid

def verify_result_exists(monitoring_id):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM results WHERE monitoring_id=?", (monitoring_id,))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    except sqlite3.Error as e:
        print(f"Error al verificar resultados en la base de datos: {e}")
        return False

def generate_id():
    return hashlib.sha256(str(uuid.uuid4()).encode('utf-8')).hexdigest()[:64]

def create_result(monitoring_id, averages):
    if verify_result_exists(monitoring_id):
        print(f"El resultado general para el monitoreo con ID {monitoring_id} ya existe.")
        return

    try:
        result_id = generate_id()

        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO results (
                id, monitoring_id, humidity, temperature, conductivity, ph, 
                nitrogen, phosphorus, potassium
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            result_id,
            monitoring_id,
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
        print(f"Resultado para el monitoreo {monitoring_id} insertado con éxito.")
    
    except sqlite3.Error as e:
        print(f"Error al insertar resultado en la base de datos: {e}")

def get_result_id(monitoring_id):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id FROM results WHERE monitoring_id = ?
        ''', (monitoring_id,))
        
        result = cursor.fetchone()  
        
        conn.close()
        
        if result:
            return result[0]
        else:
            print(f"No se encontró un resultado para el monitoring_id {monitoring_id}.")
            return None

    except sqlite3.Error as e:
        print(f"Error al recuperar el ID del resultado: {e}")
        return None


