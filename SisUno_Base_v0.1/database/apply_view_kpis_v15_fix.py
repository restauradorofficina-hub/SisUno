#!/usr/bin/env python3
# ==========================================================
# SisUno - v1.5 (correção)
# Script: apply_view_kpis_v15_fix.py
# Função: Corrige a view vw_kpis_v15 (erro de coluna pr.id_pessoa)
# ==========================================================

import sqlite3
import os

DB_PATH = "sisuno_test.db"

SQL_FIX = """
-- Corrigir view vw_kpis_v15 (ajuste no relacionamento com prontuarios)
DROP VIEW IF EXISTS vw_kpis_v15;

CREATE VIEW vw_kpis_v15 AS
SELECT
    -- Total de receitas (entradas)
    COALESCE(SUM(CASE WHEN tipo = 'receita' THEN valor ELSE 0 END), 0) AS receita_total,

    -- Total de despesas (saídas)
    COALESCE(SUM(CASE WHEN tipo = 'despesa' THEN valor ELSE 0 END), 0) AS despesa_total,

    -- Saldo consolidado
    COALESCE(SUM(CASE WHEN tipo = 'receita' THEN valor ELSE -valor END), 0) AS saldo_total,

    -- Contagem de orçamentos
    (SELECT COUNT(*) FROM orcamentos) AS total_orcamentos,

    -- Contagem de clientes (ajuste no campo de ligação)
    (SELECT COUNT(DISTINCT p.id)
     FROM pessoas p
     INNER JOIN prontuarios pr
         ON pr.id_cliente = p.id) AS total_clientes
FROM financeiro;
"""

print("========================================")
print("🧩 Correção da View vw_kpis_v15 - SisUno v1.5")
print("========================================")

if not os.path.exists(DB_PATH):
    print(f"❌ Banco de dados não encontrado: {DB_PATH}")
    exit(1)

try:
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SQL_FIX)
    conn.commit()
    print("✅ View 'vw_kpis_v15' corrigida com sucesso!")
except Exception as e:
    print(f"❌ Erro ao corrigir view: {e}")
finally:
    conn.close()

print("========================================")
print("🏁 Processo concluído.")
print("========================================")
