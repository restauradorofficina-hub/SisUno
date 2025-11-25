import sqlite3

conn = sqlite3.connect("sisuno_test.db")
with open("fix_table_financeiro_v11.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("✅ Tabela 'financeiro' reconstruída com constraint de chave estrangeira aplicada com sucesso!")
