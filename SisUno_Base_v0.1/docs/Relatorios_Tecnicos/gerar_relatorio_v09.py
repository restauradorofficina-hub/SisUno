
# ========================================
# 🧩 SisUno v0.9 - Gerador de Documento Técnico (PDF)
# ========================================

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import os

# Caminho onde o arquivo PDF será salvo
output_path = os.path.join(os.getcwd(), "SisUno_v0.9_Documento_Tecnico.pdf")

# Configuração do documento PDF
doc = SimpleDocTemplate(output_path, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# =====================================================
# Cabeçalho
# =====================================================
story.append(Paragraph("🧩 SisUno v0.9 – Documento Técnico Consolidado", styles["Title"]))
story.append(Spacer(1, 12))

intro = """
A versão 0.9 do sistema <b>SisUno</b> marca a integração total entre os módulos de <b>Custos Operacionais</b> e <b>Orçamentos</b>.
Esta atualização permite o cálculo automático dos custos de mão de obra, deslocamento e despesas fixas diretamente
a partir das tabelas <i>custos_base</i> e <i>custos_veiculo</i>, garantindo maior precisão e agilidade na formação de preços.
"""
story.append(Paragraph(intro, styles["BodyText"]))
story.append(Spacer(1, 12))

# =====================================================
# Estrutura do banco de dados
# =====================================================
story.append(Paragraph("📘 Estrutura Atualizada do Banco de Dados", styles["Heading2"]))

data = [
    ["Tabela", "Descrição"],
    ["custos_base", "Registra custos operacionais fixos e variáveis da empresa."],
    ["custos_veiculo", "Armazena os custos médios de deslocamento e operação de veículos."],
    ["orcamentos", "Agora inclui cálculos automáticos de custos e margens de lucro."]
]

tabela = Table(data, colWidths=[150, 330])
tabela.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('GRID', (0, 0), (-1, -1), 0.25, colors.grey)
]))
story.append(tabela)
story.append(Spacer(1, 12))

# =====================================================
# Destaques técnicos
# =====================================================
story.append(Paragraph("⚙️ Destaques Técnicos da Versão", styles["Heading2"]))
points = [
    "- Integração automática dos custos nas estimativas de orçamento.",
    "- Adição das colunas `custo_mdo`, `custo_deslocamento`, `custo_despesas`, `margem_lucro` e `valor_calculado`.",
    "- Atualização do módulo de cálculo para uso direto de dados das tabelas de custos.",
    "- Teste de integração validado com inserção e leitura automática.",
    "- Base preparada para geração de relatórios financeiros consolidados (v1.0)."
]
for p in points:
    story.append(Paragraph(p, styles["BodyText"]))
story.append(Spacer(1, 12))

# =====================================================
# Procedimentos de atualização
# =====================================================
story.append(Paragraph("🔧 Procedimentos de Atualização", styles["Heading2"]))
update_steps = """
1. Salvar o script <b>update_table_orcamentos_v09.sql</b> no diretório <b>/database</b>.<br/>
2. Executar <b>update_database_v09.py</b> para aplicar as novas colunas.<br/>
3. Testar a integração com <b>test_orcamentos_v09.py</b>.<br/>
4. Confirmar a operação de cálculo via <b>calcular_custos_orcamento.py</b>.
"""
story.append(Paragraph(update_steps, styles["BodyText"]))
story.append(Spacer(1, 12))

# =====================================================
# Status do projeto
# =====================================================
story.append(Paragraph("📊 Status Geral do Projeto", styles["Heading2"]))
status = """
Com a conclusão da v0.9, o SisUno atinge um patamar funcional de integração total entre os módulos operacionais e
financeiros, permitindo análise de custos em tempo real e servindo de base para relatórios e dashboards gerenciais.
A próxima versão (v1.0) focará na camada visual e na usabilidade.
"""
story.append(Paragraph(status, styles["BodyText"]))
story.append(Spacer(1, 20))

# =====================================================
# Rodapé
# =====================================================
story.append(Paragraph("📅 Data: 09/11/2025", styles["Normal"]))
story.append(Paragraph("👤 Responsável Técnico: Equipe de Desenvolvimento SisUno", styles["Normal"]))

# Geração do PDF
doc.build(story)

print("✅ Documento técnico 'SisUno_v0.9_Documento_Tecnico.pdf' gerado com sucesso!")
print("📂 Caminho:", output_path)
