# test_relatorios_v15.py
import sqlite3, datetime

print("========================================")
print("🧪 Teste Relatórios v1.5")
print("========================================")

db = "sisuno_test.db"
conn = sqlite3.connect(db)
cur = conn.cursor()

views = ["vw_resumo_mensal_v15", "vw_kpis_v15", "vw_cliente_detalhado_v15"]
for v in views:
    try:
        cur.execute(f"SELECT COUNT(*) FROM {v}")
        n = cur.fetchone()[0]
        print(f"✅ {v} -> {n} linhas")
    except Exception as e:
        print(f"❌ Erro em {v}: {e}")

conn.close()
print("========================================")
print("🏁 Teste finalizado:", datetime.datetime.now())
print("========================================")
