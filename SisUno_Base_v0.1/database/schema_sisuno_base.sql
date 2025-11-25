-- ==========================================================
--  Projeto: SisUno – Sistema Único de Gestão Integrada
--  Versão: 1.0 (Base)
--  Banco: SQLite (compatível com PostgreSQL)
-- ==========================================================

PRAGMA foreign_keys = ON;

-- =========================
-- TABELA: PESSOAS
-- =========================
CREATE TABLE pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT CHECK(tipo IN ('FISICA', 'JURIDICA')) NOT NULL,
    nome TEXT NOT NULL,
    documento TEXT,
    telefone TEXT,
    email TEXT,
    endereco TEXT,
    cidade TEXT,
    uf TEXT,
    papeis TEXT CHECK(papeis IN ('CLIENTE', 'FORNECEDOR', 'AMBOS')) DEFAULT 'CLIENTE',
    observacoes TEXT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- TABELA: OBJETOS / PEÇAS / PRODUTOS
-- =========================
CREATE TABLE objetos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('PECA', 'PRODUTO', 'OBJETO')),
    codigo_interno TEXT,
    valor_base REAL DEFAULT 0,
    observacoes TEXT
);

-- =========================
-- TABELA: SERVIÇOS / TAREFAS
-- =========================
CREATE TABLE servicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    categoria TEXT,
    valor_hora REAL DEFAULT 0,
    observacoes TEXT
);

-- =========================
-- TABELA: ORÇAMENTOS
-- =========================
CREATE TABLE orcamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    data_orcamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT,
    valor_total REAL DEFAULT 0,
    status TEXT CHECK(status IN ('ABERTO', 'FECHADO', 'CANCELADO')) DEFAULT 'ABERTO',
    observacoes TEXT,
    FOREIGN KEY (id_cliente) REFERENCES pessoas(id)
);

-- =========================
-- TABELA: ITENS DO ORÇAMENTO
-- =========================
CREATE TABLE orcamento_itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_orcamento INTEGER NOT NULL,
    tipo_item TEXT CHECK(tipo_item IN ('SERVICO', 'OBJETO')),
    id_item INTEGER NOT NULL,
    quantidade REAL DEFAULT 1,
    valor_unitario REAL DEFAULT 0,
    subtotal REAL GENERATED ALWAYS AS (quantidade * valor_unitario) STORED,
    FOREIGN KEY (id_orcamento) REFERENCES orcamentos(id)
);

-- =========================
-- TABELA: LANÇAMENTOS FINANCEIROS
-- =========================
CREATE TABLE financeiro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT CHECK(tipo IN ('RECEITA', 'DESPESA')) NOT NULL,
    categoria TEXT,
    descricao TEXT,
    valor REAL DEFAULT 0,
    data_lancamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_orcamento INTEGER,
    forma_pagamento TEXT,
    observacoes TEXT,
    FOREIGN KEY (id_orcamento) REFERENCES orcamentos(id)
);

-- ==========================================================
-- FIM DO ESQUEMA BASE SISUNO
-- ==========================================================
