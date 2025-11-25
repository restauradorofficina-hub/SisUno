from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime

# Caminho de saída do PDF
output_path = "Relatorio_Tecnico_SisUno_v0.7.pdf"

# Criar canvas
pdf = canvas.Canvas(output_path, pagesize=A4)
largura, altura = A4

# Cabeçalho
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(2 * cm, altura - 2 * cm, "Relatório Técnico Consolidado - SisUno v0.7")

pdf.setFont("Helvetica", 10)
pdf.drawString(2 * cm, altura - 2.8 * cm, f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# Linha divisória
pdf.setStrokeColor(colors.grey)
pdf.line(2 * cm, altura - 3 * cm, largura - 2 * cm, altura - 3 * cm)

# Corpo do relatório
texto = """
Versão Consolidada v0.7 – Relatório Técnico do Sistema SisUno

1️⃣ Estrutura do Sistema
- Base de dados SQLite consolidada (sisuno_test.db)
- Módulos operacionais: Clientes, Prontuários, Orçamentos e Financeiro
- Backend em Python (compatível com versão 3.13.9 64-bit)
- Scripts testados e integrados até a geração de PDF de orçamentos

2️⃣ Funcionalidades Concluídas
- Criação e vinculação de prontuários a clientes
- Criação de orçamentos com itens e totalização automática
- Geração de relatórios em PDF por orçamento
- Correção e atualização de colunas no banco (prontuarios, orcamentos, orcamento_itens)
- Integração de planilhas externas de cálculo de custos e deslocamentos

3️⃣ Funcionalidades em Andamento
- Automação de importação dos custos da planilha de Mão de Obra e Veículo
- Geração automática de relatórios de produtividade e rentabilidade
- Interface visual (frontend) do SisUno em desenvolvimento futuro (v0.8)

4️⃣ Estrutura de Pastas Recomendada
- /database → Base SQLite e scripts SQL
- /src/backend → Scripts Python (operações, PDF, integração)
- /docs/Relatorios_Tecnicos → Documentação técnica e relatórios gerados
- /exports/pdf → Orçamentos exportados em PDF

5️⃣ Instruções de Arquivamento
- Salvar este arquivo como: Relatorio_Tecnico_SisUno_v0.7.pdf
- Local: H:\\Reserva\\Pessoal\\Sistema vendas e orçamento\\SisUno_Base_v0.1\\docs\\Relatorios_Tecnicos
- Manter cópias organizadas por versão (v0.1 a v0.7)
- Criar backup completo semanal da pasta /database

6️⃣ Status Atual
✅ Módulos básicos operacionais
✅ Geração de PDF funcional
✅ Estrutura de banco de dados validada
🚧 Integração das planilhas de custos em andamento
"""

pdf.setFont("Helvetica", 10)
text_obj = pdf.beginText(2 * cm, altura - 4 * cm)
for linha in texto.splitlines():
    text_obj.textLine(linha)
pdf.drawText(text_obj)

# Rodapé
pdf.setFont("Helvetica-Oblique", 8)
pdf.drawString(2 * cm, 1.5 * cm, "Documento técnico consolidado gerado automaticamente pelo sistema SisUno v0.7")

# Finaliza e salva o PDF
pdf.save()
print(f"✅ Relatório gerado com sucesso: {output_path}")
