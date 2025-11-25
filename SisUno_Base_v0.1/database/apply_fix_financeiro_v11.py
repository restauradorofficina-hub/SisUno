import sqlite3

print("========================================")
print("🧩 Aplicando correção - Tabela financeiro (v1.1)")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    with open("update_table_financeiro_v11_fix.sql", "r", encoding="utf-8") as f:
        sql_script = f.read()
        conn.executescript(sql_script)
        conn.commit()
        print("✅ Correção aplicada com sucesso!")
except Exception as e:
    print(f"❌ Erro ao aplicar correção: {e}")
finally:
    conn.close()
    print("========================================")
    print("🏁 Processo concluído.")
    print("========================================")
