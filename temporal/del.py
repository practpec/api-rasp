import sqlite3

def remove_column_from_crops():
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()
        
        # Crear una nueva tabla sin la columna `laboratories_id`
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS crops_new (
                id TEXT PRIMARY KEY,
                crop TEXT,
                humidity_min REAL,
                humidity_max REAL,
                temperature_min REAL,
                temperature_max REAL,
                conductivity_min REAL,
                conductivity_max REAL,
                ph_min REAL,
                ph_max REAL,
                nitrogen_min REAL,
                nitrogen_max REAL,
                phosphorus_min REAL,
                phosphorus_max REAL,
                potassium_min REAL,
                potassium_max REAL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        
        # Migrar los datos existentes
        cursor.execute('''
            INSERT INTO crops_new (
                id, crop, humidity_min, humidity_max, temperature_min, temperature_max,
                conductivity_min, conductivity_max, ph_min, ph_max, nitrogen_min, nitrogen_max,
                phosphorus_min, phosphorus_max, potassium_min, potassium_max, created_at
            )
            SELECT 
                id, crop, humidity_min, humidity_max, temperature_min, temperature_max,
                conductivity_min, conductivity_max, ph_min, ph_max, nitrogen_min, nitrogen_max,
                phosphorus_min, phosphorus_max, potassium_min, potassium_max, created_at
            FROM crops;
        ''')
        
        # Renombrar tablas
        cursor.execute('DROP TABLE crops;')  # Eliminar la tabla original
        cursor.execute('ALTER TABLE crops_new RENAME TO crops;')  # Renombrar la nueva tabla

        conn.commit()
        conn.close()
        print("Columna 'laboratories_id' eliminada exitosamente.")
    
    except sqlite3.Error as e:
        print(f"Error al eliminar la columna 'laboratories_id': {e}")

# Llamar a la función
remove_column_from_crops()
