from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from datetime import datetime
import hashlib
import os

# ==============================
# 📄 CONFIGURAÇÕES INICIAIS
# ==============================
output_dir = r"H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\docs\Relatorios_Tecnicos"
output_path = os.path.join(output_dir, "Relatorio_Tecnico_SisUno_v1.3.pdf")
log_file = os.path.join(output_dir, "sisuno_version_log.txt")

# ==============================
# 🧩 CONTEÚDO DO RELATÓRIO
# ==============================
report_text = """
========================================
RELATÓRIO TÉCNICO CONSOLIDADO
SISUNO – VERSÃO 1.3
========================================
📅 Data de emissão: {data}
🧑‍💻 Responsável técnico: Officina – Desenvolvimento interno
📁 Caminho de arquivamento:
{path}
========================================

1️⃣ OBJETIVO DA VERSÃO
----------------------------------------
Esta versão consolida o módulo financeiro do SisUno, conectando:
- orçamentos individuais e pacotes de orçamentos;
- controle de despesas com cartão de crédito;
- geração de faturas consolidadas com status de pagamento;
- integração com as views financeiras e de custos.

O foco é o controle unificado das operações financeiras e de clientes,
preparando o sistema para as etapas seguintes de relatórios gerenciais.

----------------------------------------
2️⃣ ESTRUTURA DO BANCO DE DADOS
----------------------------------------
Tabelas e views envolvidas:
- financeiro (reconstruída com constraint FK)
- cartao_fatura / cartao_fatura_itens
- vw_faturas_cartao_resumo
- vw_orcamentos_com_custos
- vw_resumo_financeiro (ajustada)

Campos principais adicionados:
- id_orcamento → FK em financeiro
- custo_por_km → custos_veiculo
- sincronização automática de views

----------------------------------------
3️⃣ FUNCIONALIDADES IMPLEMENTADAS
----------------------------------------
💳 **Faturas de cartão de crédito**
Permitem vincular múltiplas despesas a um cartão e emitir uma visão consolidada
das faturas por status (a pagar, pago, parcial).

📦 **Pacotes de orçamento**
Integram múltiplos orçamentos de um mesmo cliente para negociação em conjunto.

📊 **Views atualizadas**
- vw_orcamentos_com_custos: custos diretos e deslocamento.
- vw_faturas_cartao_resumo: valores consolidados por cartão e fatura.
- vw_resumo_financeiro: totalização financeira integrada.

----------------------------------------
4️⃣ RESULTADOS DE TESTES
----------------------------------------
✅ Criação de pacotes de orçamento: OK
✅ Vinculação de orçamentos ao pacote: OK
✅ Faturas e itens de cartão criados e validados: OK
✅ Views financeiras e de custo executadas com sucesso
✅ Dados consolidados em vw_faturas_cartao_resumo

🏁 Status geral: Teste financeiro v1.3 concluído com sucesso

----------------------------------------
5️⃣ ANÁLISE DE INTEGRAÇÃO
----------------------------------------
As relações entre as tabelas de custos, orçamentos e financeiro
foram validadas com sucesso.
Os relatórios consolidados permitem controle de gastos,
margens de lucro e acompanhamento de pagamentos de forma unificada.

----------------------------------------
6️⃣ INSTRUÇÕES DE ARQUIVAMENTO
----------------------------------------
📂 Diretório padrão:
H:\\Reserva\\Pessoal\\Sistema vendas e orçamento\\SisUno_Base_v0.1\\docs\\Relatorios_Tecnicos\\
📄 Nome do arquivo:
Relatorio_Tecnico_SisUno_v1.3.pdf

----------------------------------------
🔖 Observações finais:
Esta versão consolida a integração financeira e prepara o sistema
para os relatórios gerenciais da versão 1.4.
========================================
"""

# ==============================
# 🧾 CRIAÇÃO DO PDF
# ==============================
styles = getSampleStyleSheet()
doc = SimpleDocTemplate(output_path, pagesize=A4)
content = [
    Paragraph("RELATÓRIO TÉCNICO CONSOLIDADO - SISUNO v1.3", styles["Title"]),
    Spacer(1, 12),
    Paragraph(report_text.format(data=datetime.now().strftime("%Y-%m-%d %H:%M"), path=output_path), styles["BodyText"]),
    Spacer(1, 12)
]

# Assinatura digital automática
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
sign_data = f"SisUno_v1.3_{timestamp}".encode()
signature = hashlib.sha256(sign_data).hexdigest()

content.append(Spacer(1, 12))
content.append(Paragraph(f"🔐 Assinatura Digital: {signature}", styles["BodyText"]))
content.append(Paragraph(f"🕒 Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", styles["BodyText"]))
content.append(Paragraph(f"📎 Documento Oficial - Versão 1.3", styles["BodyText"]))

doc.build(content)

# ==============================
# 🪶 REGISTRO NO LOG DE VERSÕES
# ==============================
with open(log_file, "a", encoding="utf-8") as f:
    f.write(f"\n=== SISUNO v1.3 ===\n")
    f.write(f"Data: {datetime.now()}\n")
    f.write(f"Arquivo: {output_path}\n")
    f.write(f"Assinatura: {signature}\n")
    f.write(f"Descrição: Integração financeira consolidada com pacotes e cartões.\n")
    f.write("="*50 + "\n")

print("✅ Relatório técnico v1.3 gerado e assinado com sucesso!")
print(f"📂 Caminho: {output_path}")
print(f"🔐 Assinatura: {signature}")
print(f"🗒️ Registro salvo em: {log_file}")
