-- fix_table_custos_veiculo_v12c.sql
-- Reconstrução segura da tabela custos_veiculo

PRAGMA foreign_keys = OFF;

-- 1️⃣ Renomeia a tabela antiga (caso exista)
ALTER TABLE custos_veiculo RENAME TO custos_veiculo_old;

-- 2️⃣ Cria a nova estrutura correta
CREATE TABLE custos_veiculo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('automovel', 'moto', 'caminhao', 'outro')) DEFAULT 'automovel',
    consumo_km_l REAL DEFAULT 10,
    preco_combustivel REAL DEFAULT 0,
    manutencao_mensal REAL DEFAULT 0,
    ipva_anual REAL DEFAULT 0,
    seguro_anual REAL DEFAULT 0,
    depreciação_anual REAL DEFAULT 0,
    custo_por_km REAL DEFAULT 0,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 3️⃣ Copia dados antigos (se existirem)
INSERT INTO custos_veiculo (id)
SELECT id FROM custos_veiculo_old;

-- 4️⃣ Remove tabela antiga
DROP TABLE custos_veiculo_old;

PRAGMA foreign_keys = ON;
