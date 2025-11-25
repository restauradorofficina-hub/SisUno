-- =========================================
-- 🧩 SISUNO v0.6 - Estrutura de Orçamentos
-- =========================================
-- Este script adiciona as tabelas:
--   - orcamentos
--   - orcamento_itens
-- Vinculadas ao módulo de prontuários
-- =========================================

PRAGMA foreign_keys = ON;

------------------------------------------------
-- TABELA: orcamentos
------------------------------------------------
CREATE TABLE IF NOT EXISTS orcamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prontuario_id INTEGER NOT NULL,
    codigo TEXT NOT NULL UNIQUE,
    descricao TEXT,
    valor_total REAL DEFAULT 0,
    status TEXT CHECK(status IN ('EM_ELABORACAO','APROVADO','CANCELADO','CONCLUIDO')) DEFAULT 'EM_ELABORACAO',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (prontuario_id) REFERENCES prontuarios(id)
);

------------------------------------------------
-- TABELA: orcamento_itens
------------------------------------------------
CREATE TABLE IF NOT EXISTS orcamento_itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orcamento_id INTEGER NOT NULL,
    tipo_item TEXT CHECK(tipo_item IN ('PRODUTO','SERVICO','INSUMO')) NOT NULL,
    descricao TEXT NOT NULL,
    quantidade REAL DEFAULT 1,
    valor_unitario REAL DEFAULT 0,
    valor_total REAL GENERATED ALWAYS AS (quantidade * valor_unitario) VIRTUAL,
    observacao TEXT,
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id)
);

------------------------------------------------
-- VISÃO OPCIONAL: orcamentos_detalhados
-- (Facilita consultas futuras)
------------------------------------------------
CREATE VIEW IF NOT EXISTS orcamentos_detalhados AS
SELECT
    o.id AS id_orcamento,
    o.codigo,
    o.descricao AS descricao_orcamento,
    o.valor_total AS total_orcamento,
    o.status,
    o.criado_em,
    p.nome AS cliente_nome,
    pr.codigo AS prontuario_codigo,
    oi.descricao AS item_descricao,
    oi.tipo_item,
    oi.quantidade,
    oi.valor_unitario,
    oi.valor_total AS total_item
FROM orcamentos o
LEFT JOIN prontuarios pr ON o.prontuario_id = pr.id
LEFT JOIN pessoas p ON pr.cliente_id = p.id
LEFT JOIN orcamento_itens oi ON o.id = oi.orcamento_id;

------------------------------------------------
-- LOG DE ATUALIZAÇÃO
------------------------------------------------
INSERT INTO financeiro (descricao, valor, criado_em)
VALUES ('Atualização estrutura v0.6 - Orçamentos', 0, CURRENT_TIMESTAMP);

-- =========================================
-- ✅ Fim do script - v0.6
-- =========================================
