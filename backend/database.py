import psycopg2

conn = psycopg2.connect(
    host="db",
    database="testdb",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS messages(
    id SERIAL PRIMARY KEY,
    text TEXT
)
""")

conn.commit()

cur.close()
conn.close()
