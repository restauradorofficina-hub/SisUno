-- View de indicadores financeiros para o dashboard v1.5
DROP VIEW IF EXISTS vw_kpis_v15;

CREATE VIEW vw_kpis_v15 AS
SELECT
    -- Total de receitas (entradas)
    COALESCE(SUM(CASE WHEN tipo = 'receita' THEN valor ELSE 0 END), 0) AS receita_total,

    -- Total de despesas (saídas)
    COALESCE(SUM(CASE WHEN tipo = 'despesa' THEN valor ELSE 0 END), 0) AS despesa_total,

    -- Saldo consolidado
    COALESCE(SUM(CASE WHEN tipo = 'receita' THEN valor ELSE -valor END), 0) AS saldo_total,

    -- Contagem de orçamentos
    (SELECT COUNT(*) FROM orcamentos) AS total_orcamentos,

    -- Contagem de clientes (pessoas com prontuários)
    (SELECT COUNT(DISTINCT p.id)
     FROM pessoas p
     INNER JOIN prontuarios pr ON pr.id_pessoa = p.id) AS total_clientes
FROM financeiro;
