import sqlite3

conn = sqlite3.connect("sisuno_test.db")
cur = conn.cursor()

# verificar colunas existentes
cur.execute("PRAGMA table_info(orcamentos);")
cols = [c[1] for c in cur.fetchall()]
print("📋 Colunas atuais:", cols)

# adicionar a coluna 'numero' se não existir
if "numero" not in cols:
    print("🔧 Adicionando coluna 'numero' à tabela orcamentos...")
    cur.execute("ALTER TABLE orcamentos ADD COLUMN numero TEXT;")
    conn.commit()
    print("✅ Coluna adicionada com sucesso (sem restrição UNIQUE).")
else:
    print("ℹ️ A coluna 'numero' já existe - nenhuma modificação necessária.")

conn.close()
