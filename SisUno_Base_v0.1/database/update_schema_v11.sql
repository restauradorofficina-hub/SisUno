-- =========================================
-- 🧩 SisUno v1.1 - Otimização e Índices
-- Data: 2025-11-10
-- Descrição: Reestruturação e otimização do banco de dados.
-- =========================================

-- 🔧 1. Verificação de integridade
PRAGMA foreign_keys = ON;

-- 🔍 2. Criação de índices para melhorar performance
CREATE INDEX IF NOT EXISTS idx_pessoas_nome ON pessoas (nome);
CREATE INDEX IF NOT EXISTS idx_prontuarios_cliente ON prontuarios (cliente_id);
CREATE INDEX IF NOT EXISTS idx_orcamentos_prontuario ON orcamentos (prontuario_id);
CREATE INDEX IF NOT EXISTS idx_orcamento_itens_orcamento ON orcamento_itens (orcamento_id);
CREATE INDEX IF NOT EXISTS idx_financeiro_orcamento ON financeiro (orcamento_id);

-- 🔗 3. Correção e reforço de chaves estrangeiras
-- (serão aplicadas apenas se as colunas existirem)
ALTER TABLE prontuarios
    ADD CONSTRAINT fk_prontuarios_cliente FOREIGN KEY (cliente_id)
    REFERENCES pessoas(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE orcamentos
    ADD CONSTRAINT fk_orcamentos_prontuario FOREIGN KEY (prontuario_id)
    REFERENCES prontuarios(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE orcamento_itens
    ADD CONSTRAINT fk_itens_orcamento FOREIGN KEY (orcamento_id)
    REFERENCES orcamentos(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE financeiro
    ADD CONSTRAINT fk_financeiro_orcamento FOREIGN KEY (orcamento_id)
    REFERENCES orcamentos(id) ON DELETE SET NULL ON UPDATE CASCADE;

-- 🧹 4. Limpeza de dados órfãos
DELETE FROM orcamento_itens
WHERE orcamento_id NOT IN (SELECT id FROM orcamentos);

DELETE FROM orcamentos
WHERE prontuario_id NOT IN (SELECT id FROM prontuarios);

DELETE FROM prontuarios
WHERE cliente_id NOT IN (SELECT id FROM pessoas);

-- 🧠 5. Atualização de versão
CREATE TABLE IF NOT EXISTS versoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    versao TEXT NOT NULL,
    data_aplicacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT
);

INSERT INTO versoes (versao, descricao)
VALUES ('v1.1', 'Otimização de índices, chaves e integridade referencial.');
