# src/backend/gerar_orcamento_pdf.py
import os
import sqlite3
from datetime import datetime
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import cm

# === CONFIGURAÇÃO ===
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "database" / "sisuno_test.db"
CLIENTES_DIR = Path(r"H:\SisUno\Clientes")
LOGO_PATH = BASE_DIR / "design" / "logo_sisuno.png"

CLIENTES_DIR.mkdir(parents=True, exist_ok=True)

def gerar_orcamento_pdf(orcamento_id: int) -> dict:
    resultado = {"sucesso": False, "mensagem": "", "pdf_path": "", "numero_orc": ""}
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        # BUSCAR ORÇAMENTO
        query = """
            SELECT o.id, COALESCE(o.numero, o.codigo, 'ORC-' || o.id), o.valor_total, o.status, o.data_criacao,
                   p.nome, p.cidade, p.uf, pr.caminho
            FROM orcamentos o
            JOIN prontuarios pr ON pr.id = o.prontuario_id
            JOIN pessoas p ON p.id = pr.cliente_id
            WHERE o.id = ?
        """
        cur.execute(query, (orcamento_id,))
        orc = cur.fetchone()
        if not orc:
            resultado["mensagem"] = "Orçamento não encontrado."
            return resultado

        (orc_id, numero_orc, valor_total, status, data_criacao, cliente_nome, cidade, uf, pasta_prontuario) = orc

        # BUSCAR ITENS
        cur.execute("SELECT descricao, quantidade, valor_unitario FROM itens_orcamento WHERE orcamento_id = ?", (orcamento_id,))
        itens = cur.fetchall()

        # PASTA E PDF
        pasta_orc = Path(pasta_prontuario) / "orcamentos"
        pasta_orc.mkdir(parents=True, exist_ok=True)
        pdf_path = pasta_orc / f"Orcamento_{numero_orc}.pdf"

        # GERAR PDF
        doc = SimpleDocTemplate(str(pdf_path), pagesize=A4, topMargin=2*cm)
        styles = getSampleStyleSheet()
        content = []

        # Logo
        if LOGO_PATH.exists():
            content.append(Image(str(LOGO_PATH), width=2*cm, height=2*cm))
            content.append(Spacer(1, 10))

        content.append(Paragraph("ORÇAMENTO", styles['Title']))
        content.append(Spacer(1, 12))

        # Dados
        data = [
            ["Nº:", numero_orc],
            ["Cliente:", cliente_nome],
            ["Cidade/UF:", f"{cidade} / {uf}"],
            ["Status:", status],
            ["Data:", data_criacao[:10]],
        ]
        t = Table(data, colWidths=[3*cm, 10*cm])
        t.setStyle(TableStyle([('GRID', (0,0), (-1,-1), 0.5, colors.grey)]))
        content.append(t)
        content.append(Spacer(1, 20))

        # Itens
        if itens:
            data_itens = [["Descrição", "Qtd", "Unitário", "Total"]]
            total = 0
            for desc, qtd, unit in itens:
                subt = qtd * unit
                total += subt
                data_itens.append([desc, str(qtd), f"R$ {unit:,.2f}", f"R$ {subt:,.2f}"])
            data_itens.append(["", "", "TOTAL:", f"R$ {valor_total:,.2f}"])
            t_itens = Table(data_itens)
            t_itens.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2E86C1")),
                ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                ('ALIGN', (1,1), (-1,-1), 'RIGHT'),
            ]))
            content.append(t_itens)

        doc.build(content)

        resultado.update({
            "sucesso": True,
            "mensagem": "PDF gerado!",
            "pdf_path": str(pdf_path),
            "numero_orc": numero_orc
        })

        print(f"PDF gerado: {pdf_path}")
        if os.name == 'nt':
            os.startfile(str(pdf_path))

    except Exception as e:
        resultado["mensagem"] = f"Erro: {e}"
    finally:
        if conn:
            conn.close()
    return resultado

# TESTE RÁPIDO
if __name__ == "__main__":
    print("=== Gerador de Orçamentos ===")
    try:
        oid = int(input("ID do orçamento: "))
        gerar_orcamento_pdf(oid)
    except:
        print("ID inválido.")