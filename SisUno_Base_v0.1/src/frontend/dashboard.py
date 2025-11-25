# src/frontend/dashboard.py  ← DASHBOARD FINANCEIRO SISUNO 2026
import streamlit as st
from pathlib import Path
import sqlite3
import pandas as pd

# Configuração
st.set_page_config(page_title="SisUno Dashboard", layout="wide")
st.title("SisUno 2026 – Dashboard Financeiro")

# Caminho do seu banco atual
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "database" / "sisuno_test.db"

# Carrega dados do banco
@st.cache_data
def load_data():
    conn = sqlite3.connect(str(DB_PATH))
    df_clientes = pd.read_sql("SELECT * FROM pessoas", conn)
    conn.close()
    return df_clientes

df = load_data()

if df.empty:
    st.info("Nenhum cliente cadastrado ainda. Use o módulo 'Cadastrar Cliente' para começar.")
else:
    # Métricas principais (baseadas em dados reais do seu banco)
    total_clientes = len(df)
    total_telefones = df['telefone'].notna().sum()
    cidades_unicas = df['cidade'].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Clientes", total_clientes)
    col2.metric("Com Telefone", total_telefones)
    col3.metric("Cidades Atendidas", cidades_unicas)

    # Gráfico de clientes por cidade
    st.subheader("Clientes por Cidade")
    df_cidade = df['cidade'].value_counts().head(5)
    st.bar_chart(df_cidade)

    # Tabela de clientes
    st.subheader("Lista de Clientes")
    st.dataframe(df[['id', 'nome', 'telefone', 'cidade', 'uf']], use_container_width=True)

    # Placeholder para dados financeiros (integração com SisServ depois)
    st.subheader("Resumo Financeiro (Placeholder)")
    st.info("Quando integrar o SisServ, aqui vai aparecer receita, despesas e margem real. Por enquanto, use os dados de clientes como base.")