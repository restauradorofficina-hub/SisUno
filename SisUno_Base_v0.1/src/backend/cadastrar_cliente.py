# src/backend/cadastrar_cliente.py  ← BOTÃO QUE NUNCA FALHA
import sqlite3
import streamlit as st

def cadastrar_novo_cliente():
    st.subheader("Cadastrar Novo Cliente")

    with st.form("form"):
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome completo *")
            telefone = st.text_input("Telefone *")
        with col2:
            cidade = st.text_input("Cidade", "São Paulo")
            uf = st.selectbox("UF", ["SP","RJ","MG","RS","PR","BA","DF"])

        email = st.text_input("E-mail (opcional)")
        enviado = st.form_submit_button("CADASTRAR CLIENTE")

    if enviado:
        if not nome.strip() or not telefone.strip():
            st.error("Nome e telefone obrigatórios!")
        else:
            conn = sqlite3.connect("database/sisuno_test.db")
            c = conn.cursor()
            c.execute("INSERT INTO pessoas (nome, telefone, email, cidade, uf) VALUES (?, ?, ?, ?, ?)",
                      (nome, telefone, email or None, cidade, uf))
            novo_id = c.lastrowid
            conn.commit()
            conn.close()

            st.success(f"CLIENTE {nome.upper()} CADASTRADO! ID {novo_id}")
            st.balloons()

            # BOTÃO VERMELHO GIGANTE QUE FUNCIONA
            link = f"?id={novo_id}"
            st.markdown(f"""
            <div style="text-align:center;margin:30px 0">
                <a href="{link}" target="_self">
                    <button style="background:#FF0000;color:white;padding:20px 40px;font-size:24px;border:none;border-radius:12px;cursor:pointer">
                    CRIAR PRONTUÁRIO DO ID {novo_id} AGORA
                    </button>
                </a>
            </div>
            """, unsafe_allow_html=True)