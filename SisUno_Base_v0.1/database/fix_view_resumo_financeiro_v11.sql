-- fix_view_resumo_financeiro_v11.sql
DROP VIEW IF EXISTS vw_resumo_financeiro;

CREATE VIEW vw_resumo_financeiro AS
SELECT
    f.id,
    f.tipo,
    f.categoria,
    f.descricao,
    f.valor,
    f.data_lancamento,
    f.forma_pagamento,
    o.codigo AS codigo_orcamento,
    p.nome AS cliente
FROM financeiro f
LEFT JOIN orcamentos o ON f.id_orcamento = o.id
LEFT JOIN prontuarios pr ON o.prontuario_id = pr.id
LEFT JOIN pessoas p ON pr.cliente_id = p.id;
