-- View: vw_pacote_orcamento_resumo
-- Objetivo: Consolidar orçamentos por pacote de cliente

DROP VIEW IF EXISTS vw_pacote_orcamento_resumo;

CREATE VIEW vw_pacote_orcamento_resumo AS
SELECT
    po.id AS id_pacote,
    p.nome AS cliente,
    COUNT(poi.id_orcamento) AS total_orcamentos,
    SUM(o.valor_total) AS valor_total_pacote
FROM pacote_orcamento po
LEFT JOIN pessoas p ON p.id = po.id_cliente
LEFT JOIN pacote_orcamento_itens poi ON poi.id_pacote = po.id
LEFT JOIN orcamentos o ON o.id = poi.id_orcamento
GROUP BY po.id, p.nome;
