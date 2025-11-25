-- ==========================================================
-- 🔹 SISUNO v0.8 - Atualização da tabela de orçamentos
-- Adiciona campos para integração de custos e deslocamento
-- ==========================================================

ALTER TABLE orcamentos ADD COLUMN custo_total REAL DEFAULT 0;
ALTER TABLE orcamentos ADD COLUMN deslocamento_km REAL DEFAULT 0;
ALTER TABLE orcamentos ADD COLUMN deslocamento_total REAL DEFAULT 0;
ALTER TABLE orcamentos ADD COLUMN lucro_previsto REAL DEFAULT 0;
