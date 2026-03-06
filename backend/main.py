from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

class Item(BaseModel):
    text: str

def get_connection():
    return psycopg2.connect(
        host="db",
        database="testdb",
        user="postgres",
        password="postgres"
    )

@app.post("/add")
def add_item(item: Item):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO messages (text) VALUES (%s)",
        (item.text,)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "saved"}

@app.get("/messages")
def get_messages():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT text FROM messages")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows
