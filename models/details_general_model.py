import sqlite3


def insert_details_general(id_analysis, crops_zone):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        for crop in crops_zone:
            cursor.execute('''
            INSERT INTO resultados_analysis (id_analysis, cultivo, apto, detalles, porcentaje)
            VALUES (?, ?, ?, ?, ?)
            ''', (
                id_analysis,
                crop['cultivo'],
                crop['apto'],
                str(crop['detalles']),
                crop['porcentaje']
            ))

        conn.commit()
        print(f"Se han insertado {len(crops_zone)} registros en crops_zone para analisis {id_analysis}.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos en crops_zone: {e}")
    finally:
        conn.close()
