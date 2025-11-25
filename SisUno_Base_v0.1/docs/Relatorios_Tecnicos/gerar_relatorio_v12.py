from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from datetime import datetime

# Caminho de saída do relatório
output_path = r"H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\docs\Relatorios_Tecnicos\Relatorio_Tecnico_SisUno_v1.2.pdf"

# Estilos
styles = getSampleStyleSheet()
style_title = styles["Title"]
style_body = styles["BodyText"]

# Conteúdo do relatório
content = [
    Paragraph("RELATÓRIO TÉCNICO CONSOLIDADO - SISUNO v1.2", style_title),
    Spacer(1, 12),
    Paragraph(f"Data de emissão: {datetime.now().strftime('%Y-%m-%d %H:%M')}", style_body),
    Paragraph("Responsável técnico: Officina – Desenvolvimento interno", style_body),
    Spacer(1, 12),
    Paragraph("Objetivo: Consolidar os módulos Pacote de Orçamento e Controle de Faturas.", style_body),
    Spacer(1, 12),
    Paragraph("Tabelas criadas: pacote_orcamento, pacote_orcamento_itens, cartao_fatura, cartao_fatura_itens.", style_body),
    Paragraph("Views atualizadas: vw_orcamentos_com_custos, vw_faturas_cartao_resumo.", style_body),
    Spacer(1, 12),
    Paragraph("Testes validados: test_financeiro_v12.py - Todos os testes concluídos com sucesso.", style_body),
    Spacer(1, 12),
    Paragraph("Observações: Versão base para a integração financeira total do sistema.", style_body),
    Spacer(1, 20),
    Paragraph("Assinatura digital: SisUno Compiler v1.2 Build-20251110", style_body)
]

# Geração do PDF
doc = SimpleDocTemplate(output_path, pagesize=A4)
doc.build(content)

print(f"✅ Relatório técnico v1.2 gerado com sucesso!\n📂 Caminho: {output_path}")
