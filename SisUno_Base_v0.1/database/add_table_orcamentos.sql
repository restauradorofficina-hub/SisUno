-- ===============================================
-- 🧩 SisUno v0.4 - Estrutura de tabelas de Orçamentos
-- ===============================================
-- Data: 04/11/2025
-- Autor: Equipe SisUno
-- Descrição: Criação das tabelas orcamentos e orcamento_itens
-- Integradas ao módulo de prontuário do cliente.
-- ===============================================

-- 🔍 Remove tabelas anteriores, se existirem (para testes de atualização)
DROP TABLE IF EXISTS orcamento_itens;
DROP TABLE IF EXISTS orcamentos;

-- ===============================================
-- 🧾 Tabela principal: orcamentos
-- ===============================================
CREATE TABLE orcamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prontuario_id INTEGER NOT NULL,
    numero TEXT UNIQUE NOT NULL,
    data_emissao DATETIME DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT,
    valor_total REAL DEFAULT 0,
    status TEXT CHECK(status IN ('EM_NEGOCIACAO', 'APROVADO', 'CONCLUIDO', 'CANCELADO')) DEFAULT 'EM_NEGOCIACAO',
    observacoes TEXT,
    FOREIGN KEY (prontuario_id) REFERENCES prontuarios(id)
);

-- ===============================================
-- 🧾 Tabela auxiliar: orcamento_itens
-- ===============================================
CREATE TABLE orcamento_itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orcamento_id INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    quantidade REAL DEFAULT 1,
    valor_unitario REAL DEFAULT 0,
    tipo TEXT CHECK(tipo IN ('PRODUTO', 'SERVICO', 'INSUMO')) DEFAULT 'SERVICO',
    subtotal REAL GENERATED ALWAYS AS (quantidade * valor_unitario) VIRTUAL,
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id)
);

-- ===============================================
-- 🧩 Índices e integridade
-- ===============================================
CREATE INDEX idx_orcamentos_prontuario ON orcamentos(prontuario_id);
CREATE INDEX idx_itens_orcamento ON orcamento_itens(orcamento_id);

-- ===============================================
-- 🧪 Teste inicial opcional (exemplo)
-- ===============================================
-- INSERT INTO orcamentos (prontuario_id, numero, descricao, valor_total, status)
-- VALUES (1, 'ORC-0001', 'Restauração de cristaleira antiga', 0, 'EM_NEGOCIACAO');

-- INSERT INTO orcamento_itens (orcamento_id, descricao, quantidade, valor_unitario, tipo)
-- VALUES
-- (1, 'Limpeza e lixamento', 1, 150.00, 'SERVICO'),
-- (1, 'Verniz especial', 2, 45.00, 'INSUMO'),
-- (1, 'Ferragem nova', 1, 80.00, 'PRODUTO');
-- ===============================================
-- ✅ Estrutura pronta para testes e integração com backend Python.
-- ===============================================
