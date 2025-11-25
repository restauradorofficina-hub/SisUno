import sqlite3

print("🧹 Removendo view antiga vw_orcamentos_com_custos...")

conn = sqlite3.connect("sisuno_test.db")
cur = conn.cursor()

cur.execute("DROP VIEW IF EXISTS vw_orcamentos_com_custos;")
conn.commit()
conn.close()

print("✅ View 'vw_orcamentos_com_custos' removida com sucesso.")
