import psycopg2
import re

conn = psycopg2.connect(
    dbname="aminasabit",
    user="aminasabit",
    password="1342",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def is_valid_phone(phone):
    return phone.startswith('+77') and len(phone) == 12 and re.fullmatch(r'\+77\d{9}', phone)

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        name VARCHAR,
        phone VARCHAR
    );
""")
conn.commit()

cur.execute("SELECT first_name, phone_number FROM phonebook;")
users = cur.fetchall()

invalid = []

for name, phone in users:
    if is_valid_phone(phone):
        cur.execute("""
            INSERT INTO phonebook (first_name, phone_number)
            VALUES (%s, %s)
            ON CONFLICT (first_name) DO UPDATE
            SET phone_number = EXCLUDED.phone_number;
        """, (name, phone))
    else:
        invalid.append((name, phone))

conn.commit()

print(" Данные загружены из таблицы phonebook.")
if invalid:
    print("Некорректные записи:")
    for n, p in invalid:
        print(f"Имя: {n}, Телефон: {p}")
else:
    print("Все номера корректны!")

cur.close()
conn.close()