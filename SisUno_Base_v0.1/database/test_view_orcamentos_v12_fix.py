import sqlite3
from datetime import datetime

print("========================================")
print("🧪 Teste da View - vw_orcamentos_com_custos (v1.2 fix)")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    cur = conn.cursor()

    # Verifica se a view existe
    cur.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='view' AND name='vw_orcamentos_com_custos';
    """)
    view_exists = cur.fetchone()
    if not view_exists:
        print("❌ View 'vw_orcamentos_com_custos' não encontrada.")
    else:
        print("✅ View encontrada no banco de dados.")

        # Testa se a view retorna dados
        cur.execute("SELECT * FROM vw_orcamentos_com_custos LIMIT 5;")
        rows = cur.fetchall()
        col_names = [desc[0] for desc in cur.description]
        
        print(f"📋 Colunas: {', '.join(col_names)}")
        print(f"📊 Linhas retornadas: {len(rows)}")
        for row in rows:
            print("   →", row)

    conn.close()

except Exception as e:
    print(f"❌ Erro ao testar view: {e}")

print("========================================")
print(f"🏁 Teste concluído em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("========================================")
