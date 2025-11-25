-- =========================================
-- 🧩 SisUno v0.6 - Reconstrução da tabela orcamento_itens
-- =========================================
PRAGMA foreign_keys = OFF;

-- Remover versões antigas
DROP TABLE IF EXISTS orcamento_itens_antigo;
DROP TABLE IF EXISTS orcamento_itens;

-- Criar tabela no formato atualizado
CREATE TABLE orcamento_itens (
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

PRAGMA foreign_keys = ON;

-- =========================================
-- ✅ Tabela orcamento_itens reconstruída com sucesso
-- =========================================
