import sqlite3

def delete_all_crops():
    try:
        conn = sqlite3.connect('terra-test.db')
        cursor = conn.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
        tables = [
            # 'crops_result',
            # 'details_result',
            # 'results',
            # 'details_result_zone',
            # 'reads',
            # 'result_zone',
            # 'crops_zone',
            # 'zones',
            # 'monitoring'
            'data',
            'data_analysis',
            'readings',
            'resultados_analysis',
            'resultados_cultivos'
        ]
        
        # Ejecutar DELETE para vaciar cada tabla
        #Eliminar DROP TABLE IF EXISTS
        for table in tables:
            cursor.execute(f"DELETE FROM {table};")
            print(f"Tabla {table} vaciada.")
        
        # Confirmar cambios y cerrar la conexión
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error al eliminar todos los cultivos: {e}")

# Llamar a la función
delete_all_crops()


