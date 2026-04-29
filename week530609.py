import sqlite3

conn = sqlite3.connect("notes.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    text TEXT,
    tags TEXT,
    date TEXT
)
""")

def insert_note(text, tags, date):
    c.execute("INSERT INTO notes (text, tags, date) VALUES (?, ?, ?)",
              (text, ",".join(tags), date))
    conn.commit()