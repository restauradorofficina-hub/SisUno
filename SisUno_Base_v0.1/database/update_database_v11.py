import sqlite3
import os
from datetime import datetime

print("========================================")
print("🧩 Atualização do Banco de Dados - SisUno v1.1")
print("========================================")

try:
    base_path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_path, "sisuno_test.db")
    sql_path = os.path.join(base_path, "update_schema_v11.sql")

    conn = sqlite3.connect(db_path)
    with open(sql_path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()

    print("✅ Atualização de estrutura aplicada com sucesso.")
    print("📄 Script:", os.path.basename(sql_path))

    cur = conn.cursor()
    cur.execute("SELECT versao, data_aplicacao, descricao FROM versoes ORDER BY id DESC LIMIT 1;")
    versao = cur.fetchone()
    if versao:
        print(f"📦 Versão registrada: {versao[0]} ({versao[1]}) - {versao[2]}")

    conn.close()
    print("========================================")
    print("🏁 Atualização v1.1 concluída com sucesso!")
    print("========================================")

except Exception as e:
    print("❌ Erro ao aplicar atualização:", e)
