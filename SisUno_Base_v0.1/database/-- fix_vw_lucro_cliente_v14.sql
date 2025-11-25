-- fix_vw_lucro_cliente_v14.sql
DROP VIEW IF EXISTS vw_lucro_cliente_v14;

CREATE VIEW vw_lucro_cliente_v14 AS
SELECT
    p.nome AS cliente,
    o.id AS id_orcamento,
    o.descricao AS descricao_orcamento,
    o.valor_total AS receita,
    IFNULL(cb.custo_unitario, 0) + IFNULL(cv.custo_por_km, 0) AS custo_total,
    o.valor_total - (IFNULL(cb.custo_unitario, 0) + IFNULL(cv.custo_por_km, 0)) AS lucro_estimado
FROM orcamentos o
LEFT JOIN prontuarios pr ON pr.id = o.prontuario_id
LEFT JOIN pessoas p ON p.id = pr.cliente_id
LEFT JOIN custos_base cb ON cb.id = o.id
LEFT JOIN custos_veiculo cv ON cv.id = o.id
ORDER BY p.nome, o.id;
