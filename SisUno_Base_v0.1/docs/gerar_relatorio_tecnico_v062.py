from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

# Caminho de saída
DOCS_DIR = r"H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\docs"
os.makedirs(DOCS_DIR, exist_ok=True)
PDF_PATH = os.path.join(DOCS_DIR, "SisUno_Relatorio_Tecnico_v0.6.2.pdf")

# Criar PDF
c = canvas.Canvas(PDF_PATH, pagesize=A4)
width, height = A4

# === Cabeçalho ===
c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 80, "Relatório Técnico - Projeto SisUno (v0.6.2)")

c.setFont("Helvetica", 11)
c.drawString(50, height - 110, f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
c.drawString(50, height - 130, "Resumo técnico e status do desenvolvimento do sistema.")

# === Seção 1: Status geral ===
c.setFont("Helvetica-Bold", 13)
c.drawString(50, height - 170, "1. Status geral do projeto")

c.setFont("Helvetica", 11)
texto_status = [
    "O projeto SisUno atingiu a versão 0.6.2 com estrutura estável e funcional.",
    "O sistema abrange gestão de clientes, prontuários e orçamentos, com geração de PDF automatizada.",
    "Os módulos principais foram testados com sucesso, garantindo integridade entre banco de dados e scripts Python.",
]
y = height - 190
for linha in texto_status:
    c.drawString(60, y, f"- {linha}")
    y -= 20

# === Seção 2: Progresso ===
c.setFont("Helvetica-Bold", 13)
c.drawString(50, y - 20, "2. Progresso do desenvolvimento (estimado)")
y -= 40
c.setFont("Helvetica", 11)
progresso = [
    ("Planejamento e escopo definidos", 100),
    ("Modelagem e estrutura de banco de dados", 100),
    ("Módulo de clientes e prontuários", 100),
    ("Módulo de orçamentos e PDF", 100),
    ("Documentação técnica", 60),
    ("Relatórios financeiros", 0),
    ("Interface visual (frontend)", 0),
    ("Empacotamento e distribuição", 0)
]
for item, pct in progresso:
    c.drawString(60, y, f"- {item}: {pct}%")
    y -= 20

# === Seção 3: Conclusões ===
c.setFont("Helvetica-Bold", 13)
c.drawString(50, y - 20, "3. Conclusões e próximos passos")
y -= 40
c.setFont("Helvetica", 11)
texto_final = [
    "O núcleo técnico do sistema está validado e pronto para expansão funcional.",
    "A próxima versão (v0.6.3) adicionará detalhamento dos itens no PDF e relatórios analíticos.",
    "O projeto se encontra aproximadamente 62% concluído em relação ao plano geral."
]
for linha in texto_final:
    c.drawString(60, y, f"- {linha}")
    y -= 20

# === Rodapé ===
c.setFont("Helvetica-Oblique", 9)
c.drawString(50, 50, "Documento gerado automaticamente pelo SisUno - Sistema de Gestão Integrada")
c.save()

print(f"✅ Relatório técnico criado com sucesso!")
print(f"📂 Caminho: {PDF_PATH}")
