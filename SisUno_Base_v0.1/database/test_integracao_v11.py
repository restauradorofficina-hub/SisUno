import sqlite3
from datetime import datetime

print("========================================")
print("🧩 Teste de Integração - SisUno v1.1")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    cur = conn.cursor()

    # Verificar tabelas principais
    tabelas = [
        "pessoas", "prontuarios", "orcamentos", "orcamento_itens",
        "custos_base", "custos_veiculo", "financeiro"
    ]
    for t in tabelas:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{t}'")
        if cur.fetchone():
            print(f"   ✅ {t} encontrada.")
        else:
            print(f"   ❌ {t} NÃO encontrada.")

    # Verificar views
    views = ["vw_orcamentos_com_custos", "vw_resumo_financeiro"]
    for v in views:
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='view' AND name='{v}'")
        if cur.fetchone():
            print(f"   ✅ View {v} encontrada.")
        else:
            print(f"   ⚠ View {v} não encontrada.")

    # Testar execução da view financeira
    try:
        cur.execute("SELECT * FROM vw_resumo_financeiro LIMIT 3;")
        linhas = cur.fetchall()
        print(f"🧠 View vw_resumo_financeiro retornou {len(linhas)} linha(s).")
    except Exception as e:
        print(f"⚠ Erro ao executar vw_resumo_financeiro: {e}")

    # Testar vinculação orçamentos → financeiro
    cur.execute("""
        SELECT COUNT(*) FROM sqlite_master
        WHERE sql LIKE '%FOREIGN KEY (id_orcamento)%REFERENCES orcamentos%'
    """)
    if cur.fetchone()[0] > 0:
        print("🔗 Relacionamento financeiro → orcamentos validado.")
    else:
        print("⚠ Relacionamento financeiro → orcamentos ausente.")

    print("========================================")
    print("🏁 Teste de integração do SisUno v1.1 concluído!")
    print("📅 Execução:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("========================================")

except Exception as e:
    print("❌ Erro geral no teste:", e)
finally:
    conn.close()
