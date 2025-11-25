#!/usr/bin/env python3
# update_database_v10.py
# Aplica o script SQL update_database_v10.sql e mostra resultado.

import sqlite3
import os
import sys

DB_PATH = "sisuno_test.db"
SQL_FILE = "update_database_v10.sql"

print("========================================")
print("🧩 Aplicador de atualização - SisUno v1.0")
print("========================================")

# Verificações iniciais
cwd = os.getcwd()
print("Diretório atual:", cwd)
if not os.path.exists(SQL_FILE):
    print(f"❌ Arquivo SQL não encontrado: {SQL_FILE}")
    print("→ Coloque 'update_database_v10.sql' neste diretório e execute novamente.")
    sys.exit(1)

if not os.path.exists(DB_PATH):
    print(f"❌ Banco de dados não encontrado: {DB_PATH}")
    print("→ Verifique se está no diretório correto e se o arquivo do banco existe.")
    sys.exit(1)

# Executa o script SQL
try:
    conn = sqlite3.connect(DB_PATH)
    with open(SQL_FILE, "r", encoding="utf-8") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
    print("✅ Script SQL aplicado com sucesso.")
except sqlite3.Error as e:
    print("❌ Erro ao aplicar o script SQL:", e)
    conn.rollback()
    conn.close()
    sys.exit(1)

# Verificações pós-aplicação
try:
    cur = conn.cursor()
    # verificar views e tabela de versoes
    cur.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='vw_orcamentos_com_custos';")
    if cur.fetchone():
        print("✅ View 'vw_orcamentos_com_custos' presente.")
    else:
        print("⚠️ View 'vw_orcamentos_com_custos' NÃO encontrada.")

    cur.execute("SELECT name FROM sqlite_master WHERE type='view' AND name='vw_resumo_financeiro';")
    if cur.fetchone():
        print("✅ View 'vw_resumo_financeiro' presente.")
    else:
        print("⚠️ View 'vw_resumo_financeiro' NÃO encontrada.")

    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='versoes_sisuno';")
    if cur.fetchone():
        # mostrar última versão registrada
        cur.execute("SELECT versao, data_instalacao, descricao FROM versoes_sisuno ORDER BY id DESC LIMIT 1;")
        row = cur.fetchone()
        if row:
            print(f"✅ Versão registrada: {row[0]} ({row[1]})")
            print("   Descrição:", row[2])
        else:
            print("⚠️ Tabela 'versoes_sisuno' existe mas está vazia.")
    else:
        print("⚠️ Tabela 'versoes_sisuno' NÃO encontrada.")

    conn.close()
except Exception as e:
    print("❌ Erro na verificação pós-aplicação:", e)
    conn.close()
    sys.exit(1)

print("========================================")
print("🏁 Atualização v1.0 concluída com sucesso!")
print("========================================")
