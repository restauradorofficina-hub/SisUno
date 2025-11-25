# gerar_relatorio_executivo_v15.py
import sqlite3
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

DB = os.path.join(os.path.dirname(__file__), "..", "..", "database", "sisuno_test.db")
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "Relatorios_Tecnicos", "Relatorio_Executivo_SisUno_v1.5.pdf")

def df_from_sql(query):
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def build_pdf():
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(OUT, pagesize=A4)
    content = []
    content.append(Paragraph("Relatório Executivo - SisUno v1.5", styles['Title']))
    content.append(Spacer(1,12))
    content.append(Paragraph(f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    content.append(Spacer(1,12))

    # KPIs
    kpis = df_from_sql("SELECT * FROM vw_kpis_v15;").to_dict(orient='records')
    if kpis:
        kp = kpis[0]
        content.append(Paragraph("KPIs principais:", styles['Heading2']))
        rows = [["Receita Total","Despesa Total","Lucro Total","Total Faturas","Faturas Abertas"]]
        rows.append([str(kp.get("receita_total")), str(kp.get("despesa_total")), str(kp.get("lucro_total")), str(kp.get("total_faturas")), str(kp.get("faturas_abertas"))])
        t = Table(rows)
        content.append(t)
        content.append(Spacer(1,12))

    # Resumo Mensal (últimos 6 meses)
    dfm = df_from_sql("SELECT * FROM vw_resumo_mensal_v15 LIMIT 6;")
    if not dfm.empty:
        content.append(Paragraph("Resumo Mensal (6 meses):", styles['Heading2']))
        rows = [list(dfm.columns)]
        for _, r in dfm.iterrows():
            rows.append([r['mes'], f"{r['total_receitas']:.2f}", f"{r['total_despesas']:.2f}", f"{r['saldo']:.2f}"])
        content.append(Table(rows))
        content.append(Spacer(1,12))

    # Top clientes (receita)
    dfc = df_from_sql("SELECT cliente_nome, receita_total_orcamentos FROM vw_cliente_detalhado_v15 ORDER BY receita_total_orcamentos DESC LIMIT 10;")
    if not dfc.empty:
        content.append(Paragraph("Top 10 Clientes por Receita de Orçamentos:", styles['Heading2']))
        rows = [list(dfc.columns)]
        for _, r in dfc.iterrows():
            rows.append([r['cliente_nome'], f"{r['receita_total_orcamentos']:.2f}"])
        content.append(Table(rows))
        content.append(Spacer(1,12))

    doc.build(content)
    print("✅ Relatório executivo gerado:", OUT)

if __name__ == "__main__":
    build_pdf()
