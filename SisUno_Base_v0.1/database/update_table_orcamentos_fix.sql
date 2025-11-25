-- =========================================
-- 🔧 Correção de Estrutura - Tabela orcamentos (SisUno v0.6)
-- =========================================

PRAGMA foreign_keys = OFF;

-- Renomear a tabela antiga
ALTER TABLE orcamentos RENAME TO orcamentos_antigo;

-- Criar a nova tabela no formato correto
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

-- Migrar dados possíveis
INSERT INTO orcamentos (id, prontuario_id, codigo, descricao, valor_total, status, criado_em)
SELECT id, prontuario_id, numero AS codigo, descricao, valor_total, 
       CASE status
           WHEN 'EM_NEGOCIACAO' THEN 'EM_ELABORACAO'
           ELSE 'EM_ELABORACAO'
       END AS status,
       COALESCE(data_emissao, CURRENT_TIMESTAMP)
FROM orcamentos_antigo;

DROP TABLE orcamentos_antigo;

PRAGMA foreign_keys = ON;

-- =========================================
-- ✅ Correção concluída
-- =========================================
