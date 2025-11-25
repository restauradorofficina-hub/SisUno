-- vw_kpis_v15.sql
DROP VIEW IF EXISTS vw_kpis_v15;

CREATE VIEW vw_kpis_v15 AS
SELECT
    (SELECT IFNULL(SUM(valor),0) FROM financeiro WHERE tipo='receita') AS receita_total,
    (SELECT IFNULL(SUM(valor),0) FROM financeiro WHERE tipo='despesa') AS despesa_total,
    (SELECT IFNULL(SUM(valor),0) FROM financeiro WHERE tipo='receita') -
      (SELECT IFNULL(SUM(valor),0) FROM financeiro WHERE tipo='despesa') AS lucro_total,
    (SELECT COUNT(*) FROM cartao_fatura WHERE status IN ('Aberta','Fechada')) AS total_faturas,
    (SELECT COUNT(*) FROM cartao_fatura WHERE status='Aberta') AS faturas_abertas;
