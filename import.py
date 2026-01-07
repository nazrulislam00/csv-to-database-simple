import csv
import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")

with open("data.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", row)

conn.commit()
conn.close()

print("CSV data imported successfully")
