-- vw_cliente_detalhado_v15.sql
DROP VIEW IF EXISTS vw_cliente_detalhado_v15;

CREATE VIEW vw_cliente_detalhado_v15 AS
SELECT
    p.id AS cliente_id,
    p.nome AS cliente_nome,
    COUNT(DISTINCT o.id) AS total_orcamentos,
    IFNULL(SUM(o.valor_total), 0) AS receita_total_orcamentos,
    IFNULL(SUM(f.valor), 0) AS lancamentos_financeiro_total
FROM pessoas p
LEFT JOIN prontuarios pr ON pr.cliente_id = p.id
LEFT JOIN orcamentos o ON o.prontuario_id = pr.id
LEFT JOIN financeiro f ON f.id_orcamento = o.id
GROUP BY p.id, p.nome;
