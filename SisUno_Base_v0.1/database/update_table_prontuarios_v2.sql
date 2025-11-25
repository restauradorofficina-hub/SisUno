-- ===============================================
-- 🧩 SisUno - Atualização v0.3.2
-- Correção de estrutura da tabela PRONTUARIOS
-- Adiciona campo cliente_id e reestrutura tabela.
-- ===============================================

PRAGMA foreign_keys = OFF;

-- Renomeia a tabela antiga (se existir)
ALTER TABLE prontuarios RENAME TO prontuarios_antigo;

-- Cria nova tabela completa
CREATE TABLE prontuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    codigo TEXT UNIQUE NOT NULL,
    descricao TEXT,
    caminho TEXT,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES pessoas(id)
);

-- Copia os dados antigos, preenchendo lacunas com valores padrão
INSERT INTO prontuarios (id, cliente_id, codigo, descricao, caminho, criado_em)
SELECT 
    id,
    1 AS cliente_id,  -- vincula provisoriamente ao cliente ID 1 (João Silva)
    codigo,
    COALESCE(descricao, 'Sem descrição'),
    COALESCE(caminho, 'H:\SisUno\Clientes\Desconhecido'),
    COALESCE(criado_em, CURRENT_TIMESTAMP)
FROM prontuarios_antigo;

-- Remove tabela antiga
DROP TABLE prontuarios_antigo;

PRAGMA foreign_keys = ON;
