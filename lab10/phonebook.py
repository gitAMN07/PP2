import psycopg2
import csv

conn = psycopg2.connect(
    dbname="aminasabit",
    user="aminasabit",
    password="1342",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        phone_number VARCHAR(20)
    );
""")
conn.commit()
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s);", (name, phone))
    conn.commit()
    print("Entry added.")
def insert_from_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s);", (row[0], row[1]))
    conn.commit()
    print("CSV data loaded.")
def update_entry(name, new_name=None, new_phone=None):
    if new_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s;", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone_number = %s WHERE first_name = %s;", (new_phone, new_name or name))
    conn.commit()
    print("Entry updated.")
def search(filter_by="name", value=""):
    if filter_by == "name":
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s;", (f"%{value}%",))
    elif filter_by == "phone":
        cur.execute("SELECT * FROM phonebook WHERE phone_number ILIKE %s;", (f"%{value}%",))
    rows = cur.fetchall()
    for r in rows:
        print(r)
def delete_by_value(field, value):
    if field == "name":
        cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (value,))
    elif field == "phone":
        cur.execute("DELETE FROM phonebook WHERE phone_number = %s;", (value,))
    conn.commit()
    print("Entry deleted.")
cur.close()
conn.close()