import sqlite3
from datetime import datetime

# Caminho do banco de dados
db_path = r"H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\database\sisuno_test.db"

print("========================================")
print("🧩 Teste do Módulo de Orçamentos - SisUno v0.4")
print("========================================")

try:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 🔍 Localiza o prontuário existente (assumindo que foi criado antes)
    cur.execute("SELECT id, cliente_id FROM prontuarios LIMIT 1;")
    prontuario = cur.fetchone()

    if not prontuario:
        print("❌ Nenhum prontuário encontrado. Crie um antes de testar o módulo de orçamentos.")
    else:
        prontuario_id = prontuario[0]
        cliente_id = prontuario[1]
        print(f"📁 Prontuário encontrado: ID {prontuario_id} (Cliente ID {cliente_id})")

        # 🧾 Cria orçamento de teste
        numero_orc = f"ORC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        cur.execute("""
            INSERT INTO orcamentos (prontuario_id, numero, descricao, valor_total, status)
            VALUES (?, ?, ?, 0, 'EM_NEGOCIACAO');
        """, (prontuario_id, numero_orc, "Restauração de cristaleira antiga"))

        orcamento_id = cur.lastrowid
        print(f"🧾 Orçamento criado: {numero_orc} (ID {orcamento_id})")

        # 🧩 Insere itens do orçamento
        itens = [
            ("Limpeza e lixamento", 1, 150.00, "SERVICO"),
            ("Verniz especial", 2, 45.00, "INSUMO"),
            ("Ferragem nova", 1, 80.00, "PRODUTO"),
        ]
        for desc, qtd, valor, tipo in itens:
            cur.execute("""
                INSERT INTO orcamento_itens (orcamento_id, descricao, quantidade, valor_unitario, tipo)
                VALUES (?, ?, ?, ?, ?);
            """, (orcamento_id, desc, qtd, valor, tipo))

        # 💰 Calcula o total e atualiza o orçamento
        cur.execute("""
            UPDATE orcamentos
            SET valor_total = (SELECT SUM(quantidade * valor_unitario)
                               FROM orcamento_itens WHERE orcamento_id = ?)
            WHERE id = ?;
        """, (orcamento_id, orcamento_id))

        # 🔎 Consulta final
        cur.execute("SELECT numero, descricao, valor_total, status FROM orcamentos WHERE id = ?;", (orcamento_id,))
        orc = cur.fetchone()
        print("\n📋 Resumo do orçamento gerado:")
        print(f"   Número: {orc[0]}")
        print(f"   Descrição: {orc[1]}")
        print(f"   Valor total: R$ {orc[2]:.2f}")
        print(f"   Status: {orc[3]}")

        conn.commit()
        print("\n✅ Teste de orçamentos concluído com sucesso!")

except Exception as e:
    print("❌ Erro ao testar módulo de orçamentos:", e)

finally:
    conn.close()

print("========================================")
