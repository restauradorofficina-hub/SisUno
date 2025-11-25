-- ==========================================================
-- 🔹 SISUNO v0.8 - Tabela de Custos Base
-- Contém custos de mão de obra, encargos e despesas fixas
-- ==========================================================

CREATE TABLE IF NOT EXISTS custos_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('MDO', 'FIXO', 'COMERCIAL', 'GERAL')) DEFAULT 'GERAL',
    valor REAL NOT NULL,
    data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
);
