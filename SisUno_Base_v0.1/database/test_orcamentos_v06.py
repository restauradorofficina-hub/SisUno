"""
========================================
🧩 Teste do Módulo de Orçamentos - SisUno v0.6
========================================
Objetivo:
Verificar se as tabelas `orcamentos` e `orcamento_itens`
foram criadas corretamente e se estão vinculadas a `prontuarios`.
========================================
"""

import sqlite3
from datetime import datetime

print("========================================")
print("🧩 Teste do Módulo de Orçamentos - SisUno v0.6")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    cur = conn.cursor()

    # Verificar se as tabelas foram criadas
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = [t[0] for t in cur.fetchall()]

    esperadas = {"orcamentos", "orcamento_itens", "prontuarios"}
    faltando = esperadas - set(tabelas)

    if faltando:
        raise Exception(f"Tabelas ausentes: {faltando}")

    print("✅ Estrutura de tabelas encontrada corretamente.")
    print("📋 Tabelas detectadas:", ", ".join(sorted(tabelas)))

    # Verificar se há prontuário cadastrado
    cur.execute("SELECT id, codigo FROM prontuarios LIMIT 1;")
    prontuario = cur.fetchone()
    if not prontuario:
        raise Exception("Nenhum prontuário encontrado. Crie um antes de testar.")

    prontuario_id, prontuario_codigo = prontuario
    print(f"📂 Usando prontuário de teste: {prontuario_codigo}")

    # Criar orçamento de teste
    codigo_orc = f"ORC-{int(datetime.now().timestamp())}"
    cur.execute("""
        INSERT INTO orcamentos (prontuario_id, codigo, descricao, valor_total, status)
        VALUES (?, ?, ?, ?, ?)
    """, (prontuario_id, codigo_orc, "Orçamento teste automático", 0, "EM_ELABORACAO"))
    conn.commit()

    cur.execute("SELECT id FROM orcamentos WHERE codigo = ?", (codigo_orc,))
    orc_id = cur.fetchone()[0]
    print(f"🧾 Orçamento criado com sucesso: {codigo_orc} (ID {orc_id})")

    # Inserir itens de teste
    itens_teste = [
        ("SERVICO", "Restauração de cristaleira", 1, 450.00, "Serviço principal"),
        ("INSUMO", "Verniz premium", 2, 85.50, "Material auxiliar")
    ]
    for tipo, desc, qtd, val, obs in itens_teste:
        cur.execute("""
            INSERT INTO orcamento_itens (orcamento_id, tipo_item, descricao, quantidade, valor_unitario, observacao)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (orc_id, tipo, desc, qtd, val, obs))

    conn.commit()

    # Calcular valor total e atualizar orçamento
    cur.execute("SELECT SUM(valor_total) FROM orcamento_itens WHERE orcamento_id = ?", (orc_id,))
    total = cur.fetchone()[0] or 0
    cur.execute("UPDATE orcamentos SET valor_total = ?, atualizado_em = CURRENT_TIMESTAMP WHERE id = ?", (total, orc_id))
    conn.commit()

    print(f"💰 Total calculado: R$ {total:.2f}")
    print("✅ Teste do módulo de orçamentos concluído com sucesso!")

except Exception as e:
    print(f"❌ Erro ao testar módulo de orçamentos: {e}")

finally:
    conn.close()
    print("========================================")
