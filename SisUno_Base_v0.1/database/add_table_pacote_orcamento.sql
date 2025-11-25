-- ==========================================================
-- Tabela de Pacotes de Orçamento (v1.2)
-- Agrupa múltiplos orçamentos de um mesmo cliente
-- ==========================================================

CREATE TABLE IF NOT EXISTS pacote_orcamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    valor_total REAL DEFAULT 0,
    status TEXT DEFAULT 'Aberto',
    FOREIGN KEY (id_cliente) REFERENCES pessoas(id)
);

-- ==========================================================
-- Tabela de Itens de Pacote de Orçamento
-- ==========================================================
CREATE TABLE IF NOT EXISTS pacote_orcamento_itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pacote INTEGER NOT NULL,
    id_orcamento INTEGER NOT NULL,
    FOREIGN KEY (id_pacote) REFERENCES pacote_orcamento(id),
    FOREIGN KEY (id_orcamento) REFERENCES orcamentos(id)
);
