import sqlite3

conn = sqlite3.connect("terra-test.db")
cursor = conn.cursor()

with open("terra.sql", "r") as sql_file:
    sql_script = sql_file.read()

cursor.executescript(sql_script)

conn.commit()
conn.close()

print("Base de datos creada exitosamente.")
