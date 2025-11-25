-- ==============================================================
-- SISUNO v1.0 - Script de Atualização Consolidado
-- ==============================================================
-- Objetivo: Integrar tabelas principais e criar as views de análise
-- Autor: Equipe SisUno AI
-- Data: 2025-11-10
-- ==============================================================

PRAGMA foreign_keys = ON;

------------------------------------------------------------
-- TABELAS PRINCIPAIS
------------------------------------------------------------

-- Pessoas (clientes, fornecedores ou ambos)
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT CHECK(tipo IN ('FISICA','JURIDICA')) NOT NULL,
    nome TEXT NOT NULL,
    documento TEXT,
    telefone TEXT,
    email TEXT,
    endereco TEXT,
    cidade TEXT,
    uf TEXT,
    papeis TEXT CHECK(papeis IN ('CLIENTE','FORNECEDOR','AMBOS')) DEFAULT 'CLIENTE',
    observacoes TEXT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Prontuários
CREATE TABLE IF NOT EXISTS prontuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    codigo TEXT UNIQUE,
    descricao TEXT,
    caminho TEXT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES pessoas(id)
);

-- Orçamentos
CREATE TABLE IF NOT EXISTS orcamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prontuario_id INTEGER NOT NULL,
    codigo TEXT UNIQUE,
    descricao TEXT,
    valor_total REAL DEFAULT 0,
    status TEXT CHECK(status IN ('EM_NEGOCIACAO','APROVADO','CONCLUIDO','CANCELADO')) DEFAULT 'EM_NEGOCIACAO',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME,
    arquivo_pdf TEXT,
    FOREIGN KEY (prontuario_id) REFERENCES prontuarios(id)
);

-- Itens de orçamento
CREATE TABLE IF NOT EXISTS orcamento_itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orcamento_id INTEGER NOT NULL,
    tipo_item TEXT CHECK(tipo_item IN ('SERVICO','PECA','INSUMO')) NOT NULL,
    descricao TEXT NOT NULL,
    quantidade REAL DEFAULT 1,
    valor_unitario REAL DEFAULT 0,
    subtotal REAL GENERATED ALWAYS AS (quantidade * valor_unitario) STORED,
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id)
);

-- Tabela de custos base (serviços, hora técnica, insumos gerais)
CREATE TABLE IF NOT EXISTS custos_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    unidade TEXT,
    custo_unitario REAL DEFAULT 0,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de custos de veículos (quilometragem, combustível etc.)
CREATE TABLE IF NOT EXISTS custos_veiculo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    custo_km REAL DEFAULT 0,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Financeiro (contas a receber/pagar)
CREATE TABLE IF NOT EXISTS financeiro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT CHECK(tipo IN ('RECEITA','DESPESA')) NOT NULL,
    descricao TEXT,
    valor REAL DEFAULT 0,
    data_movimento DATETIME DEFAULT CURRENT_TIMESTAMP,
    origem TEXT,
    status TEXT CHECK(status IN ('PENDENTE','QUITADO')) DEFAULT 'PENDENTE'
);

------------------------------------------------------------
-- VIEWS DE ANÁLISE
------------------------------------------------------------

-- View: orçamentos com custos consolidados
DROP VIEW IF EXISTS vw_orcamentos_com_custos;

CREATE VIEW vw_orcamentos_com_custos AS
SELECT 
    o.id AS id_orcamento,
    o.codigo AS codigo_orcamento,
    p.nome AS cliente_nome,
    pr.codigo AS codigo_prontuario,
    o.valor_total,
    IFNULL(cb.custo_unitario, 0) AS custo_base,
    IFNULL(cv.custo_km, 0) AS custo_km,
    (o.valor_total + IFNULL(cb.custo_unitario, 0) + IFNULL(cv.custo_km, 0)) AS custo_total_estimado,
    o.status
FROM orcamentos o
LEFT JOIN prontuarios pr ON o.prontuario_id = pr.id
LEFT JOIN pessoas p ON pr.cliente_id = p.id
LEFT JOIN custos_base cb ON 1=1
LEFT JOIN custos_veiculo cv ON 1=1;

-- View: resumo financeiro
DROP VIEW IF EXISTS vw_resumo_financeiro;

CREATE VIEW vw_resumo_financeiro AS
SELECT 
    tipo,
    COUNT(*) AS total_lancamentos,
    SUM(valor) AS total_valor,
    ROUND(AVG(valor),2) AS media_valor
FROM financeiro
GROUP BY tipo;

------------------------------------------------------------
-- TABELA DE VERSÕES DO SISTEMA
------------------------------------------------------------

CREATE TABLE IF NOT EXISTS versao_sistema (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    versao TEXT NOT NULL,
    descricao TEXT,
    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO versao_sistema (versao, descricao)
VALUES ('v1.0', 'Consolidação das tabelas principais e criação das views vw_orcamentos_com_custos e vw_resumo_financeiro.');

------------------------------------------------------------
-- FINALIZAÇÃO
------------------------------------------------------------

-- Fim do script
