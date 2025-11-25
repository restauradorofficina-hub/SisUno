import sqlite3, os, datetime

print("========================================")
print("💳 Atualização do Banco de Dados - SisUno v1.3")
print("========================================")

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "sisuno_test.db")

conn = sqlite3.connect(db_path)
cur = conn.cursor()

scripts = [
    "add_columns_financeiro_v13.sql",
    "create_view_vw_faturas_cartao_resumo.sql"
]

for script in scripts:
    path = os.path.join(base_dir, script)
    print(f"📄 Aplicando script: {script} ...")
    try:
        with open(path, "r", encoding="utf-8") as f:
            cur.executescript(f.read())
        conn.commit()
        print(f"✅ {script} aplicado com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao aplicar {script}: {e}")

# Verificações rápidas
print("\n📋 Verificando nova view e colunas...")
cur.execute("PRAGMA table_info(financeiro);")
cols = [c[1] for c in cur.fetchall()]
print("Colunas em financeiro:", cols)

cur.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='vw_faturas_cartao_resumo';")
print("View 'vw_faturas_cartao_resumo' presente." if cur.fetchone() else "View 'vw_faturas_cartao_resumo' NÃO encontrada.")

print("\n========================================")
print("🏁 Atualização v1.3 finalizada.")
print(f"📅 {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
print("========================================")

conn.close()

