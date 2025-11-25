import sqlite3

print("========================================")
print("🧮 Cálculo de Custos - Integração Orçamentos v0.9")
print("========================================")

db_path = "sisuno_test.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Busca custos padrão
cur.execute("SELECT SUM(custo_unitario) FROM custos_base;")
custo_base = cur.fetchone()[0] or 0

cur.execute("SELECT AVG(custo_km) FROM custos_veiculo;")
custo_km = cur.fetchone()[0] or 0

# Calcula custo simulado (exemplo)
tempo_servico_horas = 8
distancia_km = 15

custo_mdo = custo_base * (tempo_servico_horas / len(str(custo_base) or '1'))
custo_desloc = custo_km * distancia_km
custo_total = custo_mdo + custo_desloc

print(f"🧱 Custo base total: R$ {custo_mdo:.2f}")
print(f"🚗 Custo deslocamento: R$ {custo_desloc:.2f}")
print(f"💰 Custo total estimado: R$ {custo_total:.2f}")

conn.close()
print("========================================")
