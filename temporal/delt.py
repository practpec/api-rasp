import sqlite3

def delete_all_crops():
    try:
        conn = sqlite3.connect('database/terra-test.db')
        cursor = conn.cursor()

        # Borrar todos los registros de la tabla crops
        cursor.execute("DELETE FROM crops")
        
        conn.commit()
        print("Todos los cultivos eliminados de la tabla.")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error al eliminar todos los cultivos: {e}")

# Llamar a la función
delete_all_crops()
