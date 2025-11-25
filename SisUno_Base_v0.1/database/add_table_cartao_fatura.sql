-- ==========================================================
-- Tabelas de Faturas de Cartão de Crédito (v1.2)
-- Permitem consolidar despesas parceladas e compras diversas
-- ==========================================================

CREATE TABLE IF NOT EXISTS cartao_fatura (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    banco TEXT NOT NULL,
    cartao TEXT NOT NULL,
    data_fechamento DATE NOT NULL,
    data_vencimento DATE NOT NULL,
    valor_total REAL DEFAULT 0,
    status TEXT DEFAULT 'Aberta'
);

CREATE TABLE IF NOT EXISTS cartao_fatura_itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_fatura INTEGER NOT NULL,
    id_fornecedor INTEGER,
    descricao_compra TEXT NOT NULL,
    valor REAL NOT NULL,
    parcelas INTEGER DEFAULT 1,
    parcela_atual INTEGER DEFAULT 1,
    forma_pagamento TEXT DEFAULT 'Crédito',
    vinculado_a TEXT,
    FOREIGN KEY (id_fatura) REFERENCES cartao_fatura(id),
    FOREIGN KEY (id_fornecedor) REFERENCES pessoas(id)
);
