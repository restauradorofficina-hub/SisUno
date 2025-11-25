-- ========================================
-- 🧩 Atualização SisUno v0.9
-- Integração de Custos com Orçamentos
-- ========================================

-- Adiciona colunas de custo e lucro ao orçamento
ALTER TABLE orcamentos ADD COLUMN custo_mdo REAL DEFAULT 0;
ALTER TABLE orcamentos ADD COLUMN custo_deslocamento REAL DEFAULT 0;
ALTER TABLE orcamentos ADD COLUMN custo_despesas REAL DEFAULT 0;
ALTER TABLE orcamentos ADD COLUMN margem_lucro REAL DEFAULT 0.15;
ALTER TABLE orcamentos ADD COLUMN valor_calculado REAL DEFAULT 0;
ALTER TABLE orcamentos ADD COLUMN atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP;
