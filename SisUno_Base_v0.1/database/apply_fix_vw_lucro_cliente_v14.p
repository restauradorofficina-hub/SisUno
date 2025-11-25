import sqlite3, os

DB = "sisuno_test.db"
SQLFILE = "fix_vw_lucro_cliente_v14.sql"

print("Aplicando correção da view vw_lucro_cliente_v14...")

if not os.path.exists(SQLFILE):
    print(f"❌ Arquivo SQL não encontrado: {SQLFILE}")
    raise SystemExit(1)

conn = sqlite3.connect(DB)
try:
    with open(SQLFILE, "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
    print("✅ View 'vw_lucro_cliente_v14' atualizada com sucesso.")
except Exception as e:
    print("❌ Erro ao aplicar SQL:", e)
finally:
    conn.close()
