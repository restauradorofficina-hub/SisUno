-- Corrige estrutura da tabela custos_base
ALTER TABLE custos_base ADD COLUMN unidade TEXT DEFAULT 'UN';
ALTER TABLE custos_base ADD COLUMN custo_unitario REAL DEFAULT 0;
