import psycopg2

conn = psycopg2.connect(
    dbname="aminasabit",    
    user="aminasabit",    
    password="1342",  
    host="localhost",       
    port="5432"              
)

cur = conn.cursor()

cur.execute("SELECT version();")
db_version = cur.fetchone()

print("Connected to:", db_version)

cur.close()
conn.close()