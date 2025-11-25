import sqlite3

print("========================================")
print("🧩 Teste de Integração Custos-Orçamentos - SisUno v0.9")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    cur = conn.cursor()

    cur.execute("PRAGMA table_info(orcamentos);")
    cols = [c[1] for c in cur.fetchall()]
    print("📋 Colunas encontradas:", cols)

    if "custo_mdo" in cols and "valor_calculado" in cols:
        print("✅ Estrutura de orçamentos atualizada corretamente.")
    else:
        print("❌ Estrutura incompleta - verifique update_table_orcamentos_v09.sql.")
        exit()

    cur.execute("""
        INSERT INTO orcamentos (prontuario_id, codigo, descricao, custo_mdo, custo_deslocamento, custo_despesas, margem_lucro, valor_calculado)
        VALUES (1, 'ORC-TESTE-V09', 'Teste integração de custos', 500, 120, 80, 0.15, 805)
    """)
    conn.commit()

    print("✅ Orçamento inserido com custos integrados.")
    conn.close()

    print("========================================")
    print("✅ Teste do módulo de integração v0.9 concluído com sucesso!")
    print("========================================")

except Exception as e:
    print("❌ Erro ao testar módulo de integração:", e)
    print("========================================")
