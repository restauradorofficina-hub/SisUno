-- 🔧 Correção estrutural da tabela FINANCEIRO e recriação da view vw_resumo_financeiro
PRAGMA foreign_keys = OFF;

-- Renomear tabela antiga se ainda existir
DROP TABLE IF EXISTS financeiro_tmp;
CREATE TABLE IF NOT EXISTS financeiro_tmp AS SELECT * FROM financeiro;

DROP TABLE IF EXISTS financeiro;

CREATE TABLE financeiro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT CHECK(tipo IN ('RECEITA','DESPESA')) NOT NULL,
    categoria TEXT,
    descricao TEXT,
    valor REAL DEFAULT 0,
    data_lancamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_orcamento INTEGER,
    forma_pagamento TEXT,
    observacoes TEXT,
    CONSTRAINT fk_orcamento FOREIGN KEY (id_orcamento)
        REFERENCES orcamentos (id) ON DELETE SET NULL
);

-- Restaurar dados da tabela temporária (se existirem)
INSERT INTO financeiro (tipo, categoria, descricao, valor, data_lancamento, id_orcamento, forma_pagamento, observacoes)
SELECT tipo, categoria, descricao, valor, data_lancamento, id_orcamento, forma_pagamento, observacoes
FROM financeiro_tmp;

DROP TABLE IF EXISTS financeiro_tmp;

-- 🔁 Recriar view de resumo financeiro com base na tabela atual
DROP VIEW IF EXISTS vw_resumo_financeiro;
CREATE VIEW vw_resumo_financeiro AS
SELECT
    strftime('%Y-%m', data_lancamento) AS mes,
    SUM(CASE WHEN tipo = 'RECEITA' THEN valor ELSE 0 END) AS total_receitas,
    SUM(CASE WHEN tipo = 'DESPESA' THEN valor ELSE 0 END) AS total_despesas,
    SUM(CASE WHEN tipo = 'RECEITA' THEN valor ELSE -valor END) AS saldo
FROM financeiro
GROUP BY mes
ORDER BY mes DESC;

PRAGMA foreign_keys = ON;
