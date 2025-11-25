-- drop_conflicting_views_v12.sql
-- Remove views que dependem de custos_veiculo para permitir a reconstrução

DROP VIEW IF EXISTS vw_orcamentos_com_custos;
DROP VIEW IF EXISTS vw_resumo_financeiro;
