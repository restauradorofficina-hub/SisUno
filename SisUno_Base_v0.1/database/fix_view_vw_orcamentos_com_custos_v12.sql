-- ===========================================================
-- 🔧 Correção da view vw_orcamentos_com_custos - v1.2
-- Ajuste de coluna de cliente (de id_cliente → prontuario_id)
-- ===========================================================

DROP VIEW IF EXISTS vw_orcamentos_com_custos;

CREATE VIEW vw_orcamentos_com_custos AS
SELECT 
    o.id AS id_orcamento,
    o.prontuario_id AS id_cliente,
    p.nome AS nome_cliente,
    o.codigo,
    o.descricao,
    o.valor_total,
    cb.categoria AS categoria_custo,
    cb.descricao AS descricao_custo,
    cb.custo_unitario,
    cv.custo_por_km,
    o.status,
    o.criado_em,
    o.atualizado_em
FROM orcamentos o
LEFT JOIN prontuarios p ON p.id = o.prontuario_id
LEFT JOIN custos_base cb ON cb.id = o.id
LEFT JOIN custos_veiculo cv ON cv.id = o.id;
