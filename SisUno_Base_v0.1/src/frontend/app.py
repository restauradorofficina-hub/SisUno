# src/frontend/app.py  ← VERSÃO 100% FUNCIONAL COM DASHBOARD – 17/11/2025 21:30
import streamlit as st
from pathlib import Path
import sys

# Adiciona o backend ao path do Python
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Importa as funções necessárias
from backend.add_prontuario import criar_prontuario
from backend.cadastrar_cliente import cadastrar_novo_cliente

# Configuração inicial
st.set_page_config(page_title="SisUno", layout="wide")
st.title("SisUno – Sistema de Gestão")

# Menu lateral com todas as opções, incluindo Dashboard
option = st.sidebar.selectbox("Módulos", 
    ["Criar Prontuário", "Clientes", "Cadastrar Cliente", "Dashboard", "Orçamento", "Relatórios"])

# ===================================================================
# MÓDULO CRIAR PRONTUÁRIO
# ===================================================================
if option == "Criar Prontuário":
    st.header("Criar Prontuário")
    cliente_id = st.text_input("ID do Cliente", placeholder="Ex: 7")
    descricao = st.text_input("Descrição (opcional)")
    if st.button("CRIAR PRONTUÁRIO", type="primary", use_container_width=True):
        if cliente_id and cliente_id.isdigit():
            criar_prontuario(int(cliente_id), descricao)
            st.balloons()
        else:
            st.error("Digite um ID válido")

# ===================================================================
# MÓDULO CLIENTES
# ===================================================================
elif option == "Clientes":
    st.header("Clientes Cadastrados")
    try:
        import sqlite3
        import pandas as pd
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        DB_PATH = BASE_DIR / "database" / "sisuno_test.db"
        conn = sqlite3.connect(str(DB_PATH))
        dados = conn.execute("SELECT id, nome, telefone, cidade, uf FROM pessoas ORDER BY nome").fetchall()
        conn.close()
        if dados:
            df = pd.DataFrame(dados, columns=["ID", "Nome", "Telefone", "Cidade", "UF"])
            st.dataframe(df, use_container_width=True)
            st.success(f"{len(dados)} cliente(s) encontrado(s)!")
        else:
            st.info("Nenhum cliente cadastrado ainda.")
    except Exception as e:
        st.error(f"Erro ao carregar clientes: {e}")

# ===================================================================
# MÓDULO CADASTRAR CLIENTE
# ===================================================================
elif option == "Cadastrar Cliente":
    cadastrar_novo_cliente()

# ===================================================================
# MÓDULO DASHBOARD
# ===================================================================
elif option == "Dashboard":
    st.switch_page("frontend/dashboard.py")

# ===================================================================
# MÓDULOS EM DESENVOLVIMENTO
# ===================================================================
else:
    st.header(option)
    st.info("Módulo em desenvolvimento – em breve!")

# Rodapé
st.sidebar.success("SisUno v0.1 – 100% Automático")