import psycopg2

conn = psycopg2.connect(
    dbname="aminasabit",
    user="aminasabit",
    password="1342",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

create_function_sql = """
CREATE OR REPLACE FUNCTION search_phonebook(pattern VARCHAR)
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    phone_number VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.first_name, phonebook.phone_number
    FROM phonebook
    WHERE phonebook.first_name ILIKE '%' || pattern || '%'
       OR phonebook.phone_number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
"""
cur.execute(create_function_sql)
conn.commit()
print(" Функция search_phonebook успешно создана или обновлена.\n")

search_pattern = input("Введите часть имени или номера для поиска: ")
cur.execute("SELECT * FROM search_phonebook(%s);", (search_pattern,))
results = cur.fetchall()

print(f"\nНайдено записей: {len(results)}")
for row in results:
    print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")

cur.close()
conn.close()