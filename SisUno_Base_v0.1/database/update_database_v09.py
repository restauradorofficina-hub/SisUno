import sqlite3
import os

print("========================================")
print("🧩 Atualização do Banco de Dados - SisUno v0.9")
print("========================================")

db_path = "sisuno_test.db"
sql_script = "update_table_orcamentos_v09.sql"

if not os.path.exists(db_path):
    print("❌ Banco de dados não encontrado:", db_path)
else:
    conn = sqlite3.connect(db_path)
    with open(sql_script, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
        conn.commit()
        conn.close()
    print("✅ Atualização v0.9 aplicada com sucesso.")
    print("📄 Script executado:", sql_script)

print("========================================")
