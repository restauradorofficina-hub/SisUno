from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

arquivo_pdf = "Relatorio_Tecnico_SisUno_v1.4.pdf"
doc = SimpleDocTemplate(arquivo_pdf)
styles = getSampleStyleSheet()
content = []

content.append(Paragraph("Relatório Técnico - SisUno v1.4", styles["Title"]))
content.append(Spacer(1, 20))
content.append(Paragraph("📅 Data: " + str(datetime.now()), styles["Normal"]))
content.append(Paragraph("🧩 Módulo: Relatórios e Dashboards Financeiros", styles["Normal"]))
content.append(Spacer(1, 15))
content.append(Paragraph("""
Esta versão introduz as views de consolidação financeira e inicia o módulo de relatórios automáticos.
As principais melhorias incluem:
- Criação das views vw_fluxo_caixa_v14, vw_lucro_cliente_v14 e vw_pacote_orcamento_resumo;
- Base para relatórios PDF automatizados e dashboards;
- Preparação para integração visual na v1.5.
""", styles["Normal"]))
content.append(Spacer(1, 30))
content.append(Paragraph("🖋️ Assinado digitalmente por: Restaurador Officina", styles["Italic"]))
content.append(Paragraph("© Projeto SisUno — Versão 1.4", styles["Italic"]))

doc.build(content)
print(f"✅ Relatório técnico gerado: {arquivo_pdf}")
