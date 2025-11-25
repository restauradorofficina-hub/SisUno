-- View: vw_fluxo_caixa_v14
-- Objetivo: Consolidar receitas e despesas por mês e categoria

DROP VIEW IF EXISTS vw_fluxo_caixa_v14;

CREATE VIEW vw_fluxo_caixa_v14 AS
SELECT
    strftime('%Y-%m', f.data_lancamento) AS mes,
    f.categoria,
    SUM(CASE WHEN f.tipo = 'receita' THEN f.valor ELSE 0 END) AS total_receitas,
    SUM(CASE WHEN f.tipo = 'despesa' THEN f.valor ELSE 0 END) AS total_despesas,
    SUM(CASE WHEN f.tipo = 'receita' THEN f.valor ELSE 0 END)
        - SUM(CASE WHEN f.tipo = 'despesa' THEN f.valor ELSE 0 END) AS saldo_mensal
FROM financeiro f
GROUP BY mes, f.categoria
ORDER BY mes DESC;
