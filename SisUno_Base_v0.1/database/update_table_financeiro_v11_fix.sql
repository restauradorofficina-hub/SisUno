-- ==============================================
-- CORREÇÃO ESTRUTURAL - TABELA FINANCEIRO (v1.1)
-- ==============================================

PRAGMA foreign_keys = OFF;

ALTER TABLE financeiro RENAME TO financeiro_antigo;

CREATE TABLE financeiro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    categoria TEXT,
    descricao TEXT,
    valor REAL DEFAULT 0,
    data_lancamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    orcamento_id INTEGER,
    forma_pagamento TEXT,
    observacoes TEXT,
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id)
);

INSERT INTO financeiro (
    id, tipo, categoria, descricao, valor, data_lancamento,
    orcamento_id, forma_pagamento, observacoes
)
SELECT
    id, tipo, categoria, descricao, valor, data_lancamento,
    id_orcamento, forma_pagamento, observacoes
FROM financeiro_antigo;

DROP TABLE financeiro_antigo;

PRAGMA foreign_keys = ON;
