# update_database_v15.py
import sqlite3, os, datetime

print("========================================")
print("🧩 Atualização do Banco de Dados - SisUno v1.5")
print("========================================")

db = "sisuno_test.db"
scripts = [
    "vw_resumo_mensal_v15.sql",
    "vw_kpis_v15.sql",
    "vw_cliente_detalhado_v15.sql"
]

conn = sqlite3.connect(db)
cur = conn.cursor()

base = os.path.dirname(os.path.abspath(__file__))
for s in scripts:
    path = os.path.join(base, s)
    if not os.path.exists(path):
        print(f"⚠ Arquivo ausente: {s}")
        continue
    print(f"Aplicando: {s} ...")
    try:
        with open(path, "r", encoding="utf-8") as f:
            cur.executescript(f.read())
        print(f"✅ {s} aplicado.")
    except Exception as e:
        print(f"❌ Erro ao aplicar {s}: {e}")

conn.commit()
conn.close()
print("========================================")
print("🏁 Atualização v1.5 concluída:", datetime.datetime.now())
print("========================================")
