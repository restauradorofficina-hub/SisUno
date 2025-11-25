import sqlite3
from datetime import datetime

print("========================================")
print("🧪 Teste das Views de Relatórios - SisUno v1.4")
print("========================================")

try:
    conn = sqlite3.connect("sisuno_test.db")
    cur = conn.cursor()

    views = [
        "vw_fluxo_caixa_v14",
        "vw_lucro_cliente_v14",
        "vw_pacote_orcamento_resumo"
    ]

    for v in views:
        print(f"🔍 Testando {v} ...")
        cur.execute(f"SELECT COUNT(*) FROM {v}")
        count = cur.fetchone()[0]
        print(f"✅ {v} retornou {count} linhas.")

    conn.close()
    print("========================================")
    print("🏁 Teste de relatórios concluído com sucesso!")
    print(f"📅 Execução: {datetime.now()}")
    print("========================================")

except Exception as e:
    print(f"❌ Erro no teste: {e}")
