import sqlite3
import os

# Caminhos base
base_dir = os.path.dirname(os.path.abspath(__file__))
schema_file = os.path.join(base_dir, "schema_sisuno_base_v0.3.sql")
db_file = os.path.join(base_dir, "sisuno_test.db")

print("========================================")
print("🧩 Teste do Banco de Dados SisUno (SQLite)")
print("========================================")

# Remove banco anterior (se existir)
if os.path.exists(db_file):
    os.remove(db_file)
    print("🗑️  Banco anterior removido.")

# Cria nova conexão
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Lê o arquivo SQL e executa
print("📄 Aplicando schema do banco de dados...")
with open(schema_file, "r", encoding="utf-8") as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()

# Lista as tabelas criadas
print("\n📋 Tabelas encontradas no banco de dados:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for t in tables:
    print("   -", t[0])

# Finaliza
conn.close()
print("\n✅ Banco SisUno criado e testado com sucesso!")
print(f"📁 Arquivo do banco: {db_file}")
print("========================================")
