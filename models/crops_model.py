import sqlite3

def get_crops():
    
    try:
        conn = sqlite3.connect('database/terra-test.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        query = """
        SELECT 
            id,
            crop,
            humidity_min, humidity_max,
            temperature_min, temperature_max,
            conductivity_min, conductivity_max,
            ph_min, ph_max,
            nitrogen_min, nitrogen_max,
            phosphorus_min, phosphorus_max,
            potassium_min, potassium_max,
            created_at
        FROM crops
        """
        
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        # Convertimos cada fila a un diccionario
        crops = [dict(row) for row in rows]
        return crops

    except sqlite3.Error as e:
        print(f"Error al obtener cultivos: {e}")
        return []
