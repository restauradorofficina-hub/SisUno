import sqlite3
import os
from datetime import datetime

print("========================================")
print("🧩 Atualização do Banco de Dados - SisUno v1.2")
print("========================================")

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "sisuno_test.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

scripts = [
    "add_table_pacote_orcamento.sql",
    "add_table_cartao_fatura.sql",
    "update_views_v12.sql"
]

try:
    for script in scripts:
        path = os.path.join(base_dir, script)
        print(f"📄 Aplicando script: {script} ...")
        with open(path, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        print(f"✅ {script} aplicado com sucesso.")

    conn.commit()

    print("\n📋 Verificando novas tabelas e views...")
    for nome in [
        "pacote_orcamento", 
        "pacote_orcamento_itens", 
        "cartao_fatura", 
        "cartao_fatura_itens"
    ]:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (nome,))
        if cursor.fetchone():
            print(f"✅ Tabela '{nome}' criada.")
        else:
            print(f"⚠️ Tabela '{nome}' não encontrada.")

    print("\n🏁 Atualização v1.2 concluída com sucesso!")
    print(f"📅 Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("========================================")

except Exception as e:
    print(f"❌ Erro durante a atualização: {e}")
finally:
    conn.close()
