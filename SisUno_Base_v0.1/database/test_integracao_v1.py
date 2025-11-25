# ========================================
# 🧩 Teste de Integração do Banco - SisUno v1.0
# ========================================
# Este script verifica a integridade da base SisUno:
# - Confere tabelas principais
# - Testa views criadas
# - Verifica a versão registrada
# ========================================

import sqlite3
from datetime import datetime

DB_PATH = "sisuno_test.db"

print("========================================")
print("🧩 Teste de Integração - SisUno v1.0")
print("========================================")

try:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 🔍 1. Verificar tabelas principais
    tabelas_esperadas = [
        "pessoas",
        "prontuarios",
        "orcamentos",
        "orcamento_itens",
        "custos_base",
        "custos_veiculo",
        "financeiro"
    ]

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas_existentes = [t[0] for t in cur.fetchall()]

    print("\n📋 Verificação de tabelas principais:")
    for tabela in tabelas_esperadas:
        if tabela in tabelas_existentes:
            print(f"   ✅ {tabela} encontrada.")
        else:
            print(f"   ❌ {tabela} ausente!")

    # 🔍 2. Testar views
    views_esperadas = [
        "vw_orcamentos_com_custos",
        "vw_resumo_financeiro"
    ]

    cur.execute("SELECT name FROM sqlite_master WHERE type='view';")
    views_existentes = [v[0] for v in cur.fetchall()]

    print("\n📊 Verificação de views:")
    for view in views_esperadas:
        if view in views_existentes:
            print(f"   ✅ {view} disponível.")
        else:
            print(f"   ❌ {view} ausente!")

    # 🔍 3. Testar execução das views
    print("\n🧠 Teste de execução de views:")
    for view in views_esperadas:
        if view in views_existentes:
            try:
                cur.execute(f"SELECT * FROM {view} LIMIT 3;")
                resultado = cur.fetchall()
                print(f"   ✅ {view} executada ({len(resultado)} linhas retornadas).")
            except Exception as e:
                print(f"   ⚠ Erro ao executar {view}: {e}")

    # 🔍 4. Verificar registro de versão
    print("\n📦 Verificação de versão registrada:")
    try:
        cur.execute("""
            SELECT descricao, data_registro 
            FROM versao_sistema 
            ORDER BY id DESC LIMIT 1;
        """)
        versao = cur.fetchone()
        if versao:
            print(f"   ✅ Versão mais recente: {versao[0]} (registrada em {versao[1]})")
        else:
            print("   ⚠ Nenhum registro de versão encontrado.")
    except sqlite3.Error:
        print("   ⚠ Tabela de versão não encontrada.")

    # ✅ Finalização
    print("\n========================================")
    print("🏁 Teste de integração do SisUno v1.0 concluído!")
    print(f"📅 Execução: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("========================================")

except Exception as e:
    print(f"❌ Erro ao executar teste de integração: {e}")

finally:
    if 'conn' in locals():
        conn.close()
