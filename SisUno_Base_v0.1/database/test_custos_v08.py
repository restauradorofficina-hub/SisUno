import sqlite3
from datetime import datetime

print("========================================")
print("🧩 Teste do Módulo de Custos - SisUno v0.8")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    cur = conn.cursor()

    # Inserir dados simulados na tabela custos_base
    # utiliza colunas: descricao, tipo, valor, unidade (se existir), custo_unitario (se existir), data_atualizacao ou atualizado_em
    # Para compatibilidade, usa COALESCE para data.
    cur.execute("""
        INSERT INTO custos_base (descricao, tipo, valor, unidade, custo_unitario, data_atualizacao, atualizado_em)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        "Custo hora funcionário - teste",
        "MDO",
        21.18,
        "R$/h",
        21.18,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    ))
    print("✅ Registro inserido em custos_base (simulado).")

    # Inserir dados simulados na tabela custos_veiculo
    cur.execute("""
        INSERT INTO custos_veiculo (descricao, custo_km, depreciação, manutencao, combustivel, seguro, ipva, aluguel_vaga)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Veículo de serviço (teste)",
        1.19,   # custo_km aproximado
        0.10,
        0.14,
        0.44,
        0.14,
        0.0933,
        0.0
    ))
    print("✅ Registro inserido em custos_veiculo (simulado).")

    # Contagens
    cur.execute("SELECT COUNT(*) FROM custos_base;")
    base_count = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM custos_veiculo;")
    veic_count = cur.fetchone()[0]

    conn.commit()
    conn.close()

    print(f"📊 Registros em custos_base: {base_count}")
    print(f"🚗 Registros em custos_veiculo: {veic_count}")

    print("========================================")
    print("✅ Teste do módulo de custos concluído com sucesso!")
    print("========================================")

except Exception as e:
    print("❌ Erro ao testar módulo de custos:", e)
    print("========================================")
