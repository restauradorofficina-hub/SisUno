# src/backend/add_prontuario.py  ← VERSÃO OFICIAL FINAL – 17/11/2025
import os
import sqlite3
from pathlib import Path
import streamlit as st
import datetime

def criar_prontuario(cliente_id: int, descricao: str = ""):
    try:
        # CAMINHO EXATO DA SUA MÁQUINA
        CLIENTES_DIR = Path("H:/SisUno/Clientes")
        CLIENTES_DIR.mkdir(parents=True, exist_ok=True)

        # Busca nome do cliente
        conn = sqlite3.connect("database/sisuno_test.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM pessoas WHERE id = ?", (cliente_id,))
        resultado = cursor.fetchone()
        conn.close()

        if not resultado:
            st.error(f"Cliente ID {cliente_id} não encontrado!")
            return

        nome = resultado[0].strip()
        hoje = datetime.date.today().strftime("%Y-%m-%d")
        nome_seguro = "".join(c if c.isalnum() or c in " _-" else "_" for c in nome)

        # Cria pasta do cliente + prontuário
        pasta_cliente = CLIENTES_DIR / f"{nome_seguro}_{cliente_id}_{hoje}"
        pasta_prontuario = pasta_cliente / "prontuario"
        pasta_prontuario.mkdir(parents=True, exist_ok=True)

        # Abre automaticamente
        os.startfile(str(pasta_prontuario))

        st.success(f"PRONTUÁRIO CRIADO E ABERTO!")
        st.info(f"Pasta: {pasta_prontuario}")
        st.balloons()

    except Exception as e:
        st.error(f"Erro ao criar pasta: {e}")
        st.code(str(e))
