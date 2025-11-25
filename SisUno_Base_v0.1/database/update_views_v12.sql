-- ==========================================================
-- Atualização das views financeiras (v1.2)
-- ==========================================================

DROP VIEW IF EXISTS vw_orcamentos_com_custos;
CREATE VIEW vw_orcamentos_com_custos AS
SELECT 
    o.id AS orcamento_id,
    o.id_cliente,
    p.nome AS cliente_nome,
    o.valor_total,
    o.status,
    IFNULL(po.id, NULL) AS pacote_id,
    IFNULL(po.descricao, '') AS pacote_descricao,
    IFNULL(po.status, '') AS pacote_status
FROM orcamentos o
LEFT JOIN pessoas p ON o.id_cliente = p.id
LEFT JOIN pacote_orcamento_itens poi ON poi.id_orcamento = o.id
LEFT JOIN pacote_orcamento po ON po.id = poi.id_pacote;

DROP VIEW IF EXISTS vw_resumo_financeiro;
CREATE VIEW vw_resumo_financeiro AS
SELECT
    f.id AS financeiro_id,
    f.tipo,
    f.categoria,
    f.descricao,
    f.valor,
    f.data_lancamento,
    cf.cartao AS cartao_nome,
    cf.data_vencimento,
    cf.status AS status_fatura
FROM financeiro f
LEFT JOIN cartao_fatura_itens cfi ON f.descricao = cfi.descricao_compra
LEFT JOIN cartao_fatura cf ON cf.id = cfi.id_fatura;
