-- create_view_vw_faturas_cartao_resumo.sql
DROP VIEW IF EXISTS vw_faturas_cartao_resumo;

CREATE VIEW vw_faturas_cartao_resumo AS
SELECT 
    cf.id AS id_fatura,
    cf.banco AS banco,
    cf.cartao AS nome_cartao,
    cf.data_fechamento,
    cf.data_vencimento,
    cf.valor_total,
    cf.status AS status_fatura,
    COUNT(cfi.id) AS qtd_itens,
    IFNULL(SUM(cfi.valor), 0) AS total_itens,
    IFNULL(SUM(f.valor), 0) AS total_lancado_financeiro,
    CASE 
        WHEN cf.status = 'Aberta' THEN 'A Pagar'
        WHEN cf.status = 'Paga' THEN 'Liquidada'
        ELSE cf.status
    END AS situacao
FROM cartao_fatura cf
LEFT JOIN cartao_fatura_itens cfi ON cfi.id_fatura = cf.id
LEFT JOIN financeiro f ON f.id_fatura = cf.id
GROUP BY cf.id, cf.banco, cf.cartao, cf.data_fechamento, cf.data_vencimento, cf.valor_total, cf.status;
