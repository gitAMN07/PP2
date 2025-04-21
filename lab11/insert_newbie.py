import psycopg2

conn = psycopg2.connect(
    dbname="aminasabit",
    user="aminasabit",
    password="1342",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

create_proc = """
CREATE OR REPLACE PROCEDURE upsert_phonebook(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
        UPDATE phonebook
        SET phone_number = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook (first_name, phone_number)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;
"""
cur.execute(create_proc)
conn.commit()
print("Процедура upsert_phonebook создана или обновлена.\n")

name = input("Введите имя: ")
phone = input("Введите номер телефона: ")

cur.execute("CALL upsert_phonebook(%s, %s);", (name, phone))
conn.commit()
print("Запись успешно добавлена или обновлена.")

cur.close()
conn.close()