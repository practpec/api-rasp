import sqlite3

conn = sqlite3.connect('terra-test.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS readings (
        id_analysis INTEGER,
        id_zone INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        humidity REAL,
        temperature REAL,
        conductivity REAL,
        ph REAL,
        nitrogen REAL,
        phosphorus REAL,
        potassium REAL
    )
''')
#zona
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id_analysis INTEGER,
        id_zone INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        humidity REAL,
        temperature REAL,
        conductivity REAL,
        pH REAL,
        nitrogen REAL,
        phosphorus REAL,
        potassium REAL
    )
''')
# generales
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_analysis (
        id_analysis INTEGER PRIMARY KEY,
        humidity REAL,
        temperature REAL,
        conductivity REAL,
        pH REAL,
        nitrogen REAL,
        phosphorus REAL,
        potassium REAL
    )
''')
#resultados generales
cursor.execute('''
    CREATE TABLE IF NOT EXISTS resultados_analysis (
        id_analysis INTEGER,
        cultivo TEXT,
        apto BOOLEAN,
        detalles TEXT,
        porcentaje REAL
    )
''')

#resultados por zona
cursor.execute('''
    CREATE TABLE resultados_cultivos (
        id_analysis INTEGER NOT NULL,
        id_zone INTEGER NOT NULL,
        cultivo TEXT NOT NULL,
        apto BOOLEAN NOT NULL,
        detalles TEXT NOT NULL,
        porcentaje REAL,
        PRIMARY KEY (id_analysis, id_zone, cultivo)
)
''')
#cultivos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS crops (
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
)
''')


conn.commit()
print("Tablas creadas exitosamente en terra-test.db")


conn.close()
