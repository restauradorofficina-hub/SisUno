-- =========================================
-- 🧩 SisUno v0.6 - Reconstrução completa da tabela orcamentos
-- =========================================
PRAGMA foreign_keys = OFF;

-- Remover qualquer versão antiga
DROP TABLE IF EXISTS orcamentos_antigo;
DROP TABLE IF EXISTS orcamentos;

-- Criar nova tabela conforme padrão v0.6
CREATE TABLE orcamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prontuario_id INTEGER NOT NULL,
    codigo TEXT NOT NULL UNIQUE,
    descricao TEXT,
    valor_total REAL DEFAULT 0,
    status TEXT CHECK(status IN ('EM_ELABORACAO','APROVADO','CANCELADO','CONCLUIDO')) DEFAULT 'EM_ELABORACAO',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (prontuario_id) REFERENCES prontuarios(id)
);

PRAGMA foreign_keys = ON;

-- =========================================
-- ✅ Rebuild concluído - Estrutura limpa
-- =========================================
