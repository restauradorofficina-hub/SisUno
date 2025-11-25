-- ==========================================================
-- 🔹 SISUNO v0.8 - Tabela de Custos de Veículo
-- Armazena custo operacional e total por quilômetro rodado
-- ==========================================================

CREATE TABLE IF NOT EXISTS custos_veiculo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    custo_km REAL NOT NULL,
    depreciação REAL DEFAULT 0,
    manutencao REAL DEFAULT 0,
    combustivel REAL DEFAULT 0,
    seguro REAL DEFAULT 0,
    ipva REAL DEFAULT 0,
    aluguel_vaga REAL DEFAULT 0,
    data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
);
