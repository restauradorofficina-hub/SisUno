-- ===============================================
-- 🧩 SisUno v0.3 - Script de criação da tabela "prontuarios"
-- ===============================================
-- Data: 04/11/2025
-- Autor: Equipe SisUno
-- Descrição: Estrutura complementar ao módulo de prontuário do cliente
-- ===============================================

-- 🔍 Verifica se a tabela já existe
DROP TABLE IF EXISTS prontuarios;

-- 🏗️ Cria nova tabela
CREATE TABLE prontuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    codigo TEXT UNIQUE NOT NULL,
    descricao TEXT,
    caminho TEXT NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES pessoas(id)
);

-- ✅ Exibe mensagem simulada de confirmação (em ferramentas com suporte)
-- (SQLite não exibe mensagens diretas, então é apenas ilustrativo)
-- PRINT 'Tabela "prontuarios" criada com sucesso.';

-- ===============================================
-- 🧩 Teste opcional (para validação)
-- =================================
