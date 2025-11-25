import sqlite3, datetime

print("========================================")
print("🧪 Teste Financeiro Consolidado - v1.3")
print("========================================")

conn = sqlite3.connect("sisuno_test.db")
cur = conn.cursor()

try:
    # ver quantas faturas existem
    cur.execute("SELECT COUNT(*) FROM cartao_fatura;")
    qtd = cur.fetchone()[0]
    print(f"Cartões / faturas cadastradas: {qtd}")

    # ver resumo da view consolidada
    cur.execute("SELECT id_fatura, nome_cartao, valor_total, total_itens, total_lancado_financeiro, situacao FROM vw_faturas_cartao_resumo;")
    rows = cur.fetchall()
    print("Linhas em vw_faturas_cartao_resumo:", len(rows))
    for r in rows:
        print(" →", r)

    print("\n✅ Teste executado com sucesso.")
except Exception as e:
    print("❌ Erro no teste:", e)
finally:
    conn.close()

print("========================================")
print("🏁 Fim do teste -", datetime.datetime.now())
print("========================================")
