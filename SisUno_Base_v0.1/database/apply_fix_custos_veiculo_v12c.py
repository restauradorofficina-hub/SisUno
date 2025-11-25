import sqlite3

print("========================================")
print("🧩 Correção da Tabela custos_veiculo - v1.2c")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    with open("fix_table_custos_veiculo_v12c.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())
        conn.commit()
        print("✅ Tabela 'custos_veiculo' reconstruída com sucesso!")
except Exception as e:
    print(f"❌ Erro ao aplicar correção: {e}")
finally:
    conn.close()
    print("========================================")
    print("🏁 Processo concluído.")
    print("========================================")
