-- ===============================================
-- 🧩 SisUno - Atualização de estrutura v0.3.1
-- Adiciona a coluna cliente_id à tabela prontuarios
-- ===============================================

PRAGMA foreign_keys = OFF;

-- Renomeia a tabela atual
ALTER TABLE prontuarios RENAME TO prontuarios_antigo;

-- Cria a nova tabela com a coluna cliente_id
CREATE TABLE prontuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    codigo TEXT UNIQUE NOT NULL,
    descricao TEXT,
    caminho TEXT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES pessoas(id)
);

-- Copia os dados antigos, assumindo cliente_id = 1 (ou outro fixo)
INSERT INTO prontuarios (id, cliente_id, codigo, descricao, caminho, criado_em)
SELECT id, 1 AS cliente_id, codigo, descricao, caminho, criado_em
FROM prontuarios_antigo;

-- Remove a tabela antiga
DROP TABLE prontuarios_antigo;

PRAGMA foreign_keys = ON;
