import sqlite3

print("========================================")
print("🔍 Verificação da View vw_kpis_v15")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    cur = conn.cursor()
    
    # Verifica se a view existe
    cur.execute("""
        SELECT name FROM sqlite_master
        WHERE type='view' AND name='vw_kpis_v15';
    """)
    
    view = cur.fetchone()
    if view:
        print("✅ View encontrada:", view[0])
    else:
        print("❌ View 'vw_kpis_v15' não encontrada!")
        exit()
    
    # Mostra algumas colunas e valores
    print("\n📊 Visualizando dados da view:")
    cur.execute("SELECT * FROM vw_kpis_v15;")
    row = cur.fetchone()
    print("→", row)
    
    conn.close()
except Exception as e:
    print(f"❌ Erro ao acessar view: {e}")
finally:
    print("========================================")
    print("🏁 Verificação concluída.")
    print("========================================")
