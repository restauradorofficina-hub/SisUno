import sqlite3
from datetime import datetime
import os

print("========================================")
print("🧩 Atualização do Banco de Dados - SisUno v1.4")
print("========================================")

try:
    db_path = "sisuno_test.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for sql_file in [
        "vw_fluxo_caixa_v14.sql",
        "vw_lucro_cliente_v14.sql",
        "vw_pacote_orcamento_resumo.sql"
    ]:
        if os.path.exists(sql_file):
            print(f"📄 Aplicando script: {sql_file} ...")
            with open(sql_file, "r", encoding="utf-8") as f:
                cursor.executescript(f.read())
                print(f"✅ {sql_file} aplicado com sucesso.")
        else:
            print(f"⚠ Arquivo não encontrado: {sql_file}")

    conn.commit()
    print("\n📋 Verificação de views criadas:")
    for view in ["vw_fluxo_caixa_v14", "vw_lucro_cliente_v14", "vw_pacote_orcamento_resumo"]:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='view' AND name=?", (view,))
        result = cursor.fetchone()
        if result:
            print(f"✅ View '{view}' criada.")
        else:
            print(f"❌ View '{view}' ausente.")

    conn.close()
    print("========================================")
    print("🏁 Atualização v1.4 concluída com sucesso!")
    print(f"📅 Data: {datetime.now()}")
    print("========================================")

except Exception as e:
    print(f"❌ Erro ao aplicar atualização: {e}")
