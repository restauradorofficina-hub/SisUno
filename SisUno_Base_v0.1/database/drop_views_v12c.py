import sqlite3

conn = sqlite3.connect("sisuno_test.db")

with open("drop_conflicting_views_v12.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())
    conn.commit()
    conn.close()

print("✅ Views problemáticas removidas temporariamente.")
