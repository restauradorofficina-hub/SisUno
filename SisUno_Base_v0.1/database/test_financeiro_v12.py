import sqlite3
from datetime import datetime

print("========================================")
print("💳 Teste de Integração Financeira - SisUno v1.2")
print("========================================")

conn = sqlite3.connect("sisuno_test.db")
cur = conn.cursor()

try:
    # 🔹 1. Inserir um pacote de orçamentos simulado
    cur.execute("""
        INSERT INTO pacote_orcamento (id_cliente, descricao, valor_total, status)
        VALUES (1, 'Pacote Teste - Serviços Diversos', 2500.00, 'Aberto');
    """)
    pacote_id = cur.lastrowid
    print(f"✅ Pacote de orçamento criado (ID: {pacote_id}).")

    # 🔹 2. Vincular orçamentos existentes (se houver)
    cur.execute("SELECT id FROM orcamentos LIMIT 1;")
    orc = cur.fetchone()
    if orc:
        cur.execute("""
            INSERT INTO pacote_orcamento_itens (id_pacote, id_orcamento)
            VALUES (?, ?);
        """, (pacote_id, orc[0]))
        print(f"✅ Orçamento vinculado ao pacote (ID orc: {orc[0]}).")
    else:
        print("⚠ Nenhum orçamento encontrado para vincular ao pacote.")

    # 🔹 3. Criar fatura de cartão simulada
    cur.execute("""
        INSERT INTO cartao_fatura (banco, cartao, data_fechamento, data_vencimento, valor_total, status)
        VALUES ('Banco Teste', 'Visa Gold', '2025-11-30', '2025-12-10', 1200.00, 'Aberta');
    """)
    fatura_id = cur.lastrowid
    print(f"✅ Fatura de cartão criada (ID: {fatura_id}).")

    # 🔹 4. Adicionar itens à fatura
    cur.execute("""
        INSERT INTO cartao_fatura_itens (id_fatura, descricao_compra, valor, parcelas, parcela_atual, forma_pagamento)
        VALUES (?, 'Compra de Materiais', 400.00, 3, 1, 'Crédito');
    """, (fatura_id,))
    cur.execute("""
        INSERT INTO cartao_fatura_itens (id_fatura, descricao_compra, valor, parcelas, parcela_atual, forma_pagamento)
        VALUES (?, 'Serviço de Transporte', 200.00, 1, 1, 'Débito');
    """, (fatura_id,))
    print("✅ Itens de fatura adicionados.")

    conn.commit()

    # 🔹 5. Testar views
    print("\n📊 Testando views atualizadas...")
    for view in ["vw_orcamentos_com_custos", "vw_resumo_financeiro"]:
        cur.execute(f"SELECT COUNT(*) FROM {view};")
        total = cur.fetchone()[0]
        print(f"   🔹 {view}: {total} linha(s) retornada(s).")

    print("\n🏁 Teste de integração financeira v1.2 concluído com sucesso!")
    print(f"📅 Execução: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("========================================")

except Exception as e:
    print(f"❌ Erro no teste financeiro: {e}")

finally:
    conn.close()
