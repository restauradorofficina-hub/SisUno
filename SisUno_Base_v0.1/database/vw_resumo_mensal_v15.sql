-- vw_resumo_mensal_v15.sql
DROP VIEW IF EXISTS vw_resumo_mensal_v15;

CREATE VIEW vw_resumo_mensal_v15 AS
SELECT
    strftime('%Y-%m', f.data_lancamento) AS mes,
    SUM(CASE WHEN f.tipo = 'receita' THEN f.valor ELSE 0 END) AS total_receitas,
    SUM(CASE WHEN f.tipo = 'despesa' THEN f.valor ELSE 0 END) AS total_despesas,
    SUM(CASE WHEN f.tipo = 'receita' THEN f.valor ELSE 0 END)
      - SUM(CASE WHEN f.tipo = 'despesa' THEN f.valor ELSE 0 END) AS saldo
FROM financeiro f
GROUP BY mes
ORDER BY mes DESC;
