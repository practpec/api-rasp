import sqlite3


def insert_details_zone(id_analysis, id_zone, crops_zone):
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        for crop in crops_zone:
            cursor.execute('''
            INSERT INTO resultados_cultivos (id_analysis, id_zone, cultivo, apto, detalles, porcentaje)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                id_analysis,
                id_zone,
                crop['cultivo'],
                crop['apto'],
                str(crop['detalles']),
                crop['porcentaje']
            ))

        conn.commit()
        print(f"Se han insertado {len(crops_zone)} registros en crops_zone para la zona {id_zone}.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos en crops_zone: {e}")
    finally:
        conn.close()
