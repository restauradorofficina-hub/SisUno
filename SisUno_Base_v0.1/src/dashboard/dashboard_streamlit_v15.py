# dashboard_streamlit_v15.py
import streamlit as st
import sqlite3
import pandas as pd
import os

DB = os.path.join(os.path.dirname(__file__), "..", "..", "database", "sisuno_test.db")

@st.cache_data
def query_df(q):
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query(q, conn)
    conn.close()
    return df

st.set_page_config(page_title="SisUno - Dashboard Financeiro", layout="wide")
st.title("SisUno — Dashboard Financeiro (v1.5)")

# KPIs
kpis = query_df("SELECT * FROM vw_kpis_v15;")
if not kpis.empty:
    kp = kpis.iloc[0]
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Receita Total", f"{kp['receita_total']:.2f}")
    col2.metric("Despesa Total", f"{kp['despesa_total']:.2f}")
    col3.metric("Lucro Total", f"{kp['lucro_total']:.2f}")
    col4.metric("Faturas Abertas", int(kp['faturas_abertas']))

# Filtro de período
meses = query_df("SELECT mes FROM vw_resumo_mensal_v15 ORDER BY mes DESC LIMIT 12;")
mes = st.selectbox("Mês", options=meses['mes'].tolist() if not meses.empty else [])

# Mostrar resumo mensal
if mes:
    dfm = query_df(f"SELECT * FROM vw_resumo_mensal_v15 WHERE mes = '{mes}';")
    st.subheader("Resumo do mês selecionado")
    st.dataframe(dfm)

# Top clientes
st.subheader("Top clientes (receita)")
dfc = query_df("SELECT cliente_nome, receita_total_orcamentos FROM vw_cliente_detalhado_v15 ORDER BY receita_total_orcamentos DESC LIMIT 20;")
st.table(dfc)
