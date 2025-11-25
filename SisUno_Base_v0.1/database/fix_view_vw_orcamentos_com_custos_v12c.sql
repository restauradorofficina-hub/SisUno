-- ===========================================================
-- 🔧 Correção final da view vw_orcamentos_com_custos - v1.2c
-- Removida coluna inexistente 'cb.categoria'
-- ===========================================================

DROP VIEW IF EXISTS vw_orcamentos_com_custos;

CREATE VIEW vw_orcamentos_com_custos AS
SELECT 
    o.id AS id_orcamento,
    pr.id AS id_prontuario,
    pe.nome AS nome_cliente,
    o.codigo,
    o.descricao,
    o.valor_total,
    cb.descricao AS descricao_custo,
    cb.custo_unitario,
    cv.custo_por_km,
    o.status,
    o.criado_em,
    o.atualizado_em
FROM orcamentos o
LEFT JOIN prontuarios pr ON pr.id = o.prontuario_id
LEFT JOIN pessoas pe ON pe.id = pr.pessoa_id
LEFT JOIN custos_base cb ON cb.id = o.id
LEFT JOIN custos_veiculo cv ON cv.id = o.id;
