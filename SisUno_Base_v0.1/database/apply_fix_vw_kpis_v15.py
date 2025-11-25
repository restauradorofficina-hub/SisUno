import sqlite3

print("========================================")
print("🧩 Aplicando correção da View vw_kpis_v15 (v1.5 fix)")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    with open("fix_vw_kpis_v15.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("✅ View 'vw_kpis_v15' recriada com sucesso!")
except Exception as e:
    print("❌ Erro ao aplicar correção:", e)
finally:
    print("========================================")
    print("🏁 Processo concluído.")
    print("========================================")
