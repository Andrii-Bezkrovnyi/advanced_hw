import sqlite3

DB_NAME = "university.db"
SQL_FILE = "create_university.sql"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

with open(SQL_FILE, "r", encoding="utf-8") as f:
    sql_script = f.read()

cursor.executescript(sql_script)

conn.commit()
conn.close()

print(f"Tables from '{SQL_FILE}' successfully created in '{DB_NAME}'.")
