import sqlite3
import os

# Caminho do banco de dados
DB_PATH = "sisuno_test.db"

# Lista de scripts SQL que serão aplicados
SQL_SCRIPTS = [
    "add_table_custos_base.sql",
    "add_table_custos_veiculo.sql",
    "update_table_orcamentos_v08.sql"
]

print("========================================")
print("🧩 Atualização do Banco de Dados - SisUno v0.8")
print("========================================")

# Verificar se o banco existe
if not os.path.exists(DB_PATH):
    print(f"❌ Banco de dados '{DB_PATH}' não encontrado.")
    exit(1)

# Conectar ao banco
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Aplicar cada script
for script in SQL_SCRIPTS:
    if os.path.exists(script):
        print(f"📄 Aplicando script: {script} ...")
        with open(script, "r", encoding="utf-8") as f:
            sql_content = f.read()
            try:
                cursor.executescript(sql_content)
                conn.commit()
                print(f"✅ {script} aplicado com sucesso.")
            except sqlite3.Error as e:
                print(f"❌ Erro ao aplicar {script}: {e}")
    else:
        print(f"⚠️ Arquivo {script} não encontrado. Ignorando.")

# Verificação das novas tabelas
print("\n📋 Verificando tabelas criadas/atualizadas...")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = [t[0] for t in cursor.fetchall()]
for nome in ["custos_base", "custos_veiculo", "orcamentos"]:
    if nome in tabelas:
        print(f"✅ Tabela '{nome}' detectada.")
    else:
        print(f"⚠️ Tabela '{nome}' não encontrada!")

# Encerrar
conn.close()
print("========================================")
print("🏁 Atualização v0.8 concluída!")
print("========================================")
