import sqlite3

print("🏗️  Reconstruindo view vw_orcamentos_com_custos...")

sql = """
CREATE VIEW IF NOT EXISTS vw_orcamentos_com_custos AS
SELECT
    o.id AS id_orcamento,
    o.codigo AS codigo_orcamento,
    o.descricao AS descricao_orcamento,
    o.valor_total,
    p.id AS id_prontuario,
    p.descricao AS descricao_prontuario,
    cv.custo_por_km,
    cb.descricao AS categoria_custo,
    cb.custo_unitario
FROM orcamentos o
LEFT JOIN prontuarios p ON o.prontuario_id = p.id
LEFT JOIN custos_veiculo cv ON 1 = 1
LEFT JOIN custos_base cb ON 1 = 1;
"""

conn = sqlite3.connect("sisuno_test.db")
cur = conn.cursor()
cur.executescript(sql)
conn.commit()
conn.close()

print("✅ View 'vw_orcamentos_com_custos' recriada com sucesso.")
