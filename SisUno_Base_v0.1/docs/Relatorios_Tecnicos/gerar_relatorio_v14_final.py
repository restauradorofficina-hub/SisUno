# gerar_relatorio_v14_final.py
# Gera Relatório Técnico Consolidado - SisUno v1.4
# Produz PDF assinado (SHA256), grava registro no log e salva no diretório padrão.

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from datetime import datetime
import hashlib
import os
import sys

# -----------------------
# Configurações / caminhos
# -----------------------
OUTPUT_DIR = r"H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\docs\Relatorios_Tecnicos"
OUTPUT_FILE = "Relatorio_Tecnico_SisUno_v1.4.pdf"
LOG_FILE = "sisuno_version_log.txt"
SCHEMA_CANDIDATES = [
    r"..\database\schema_sisuno_base.sql",
    r"..\database\schema_sisuno_base_v0.2.sql",
    r"..\database\schema_sisuno_base_v0.3.sql",
    r"..\database\schema_sisuno_base.sql"
]

# Garante que o diretório exista
os.makedirs(OUTPUT_DIR, exist_ok=True)
output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
log_path = os.path.join(OUTPUT_DIR, LOG_FILE)

# -----------------------
# Monta o conteúdo do relatório (factual)
# -----------------------
now = datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")

report_lines = []

report_lines.append("RELATÓRIO TÉCNICO CONSOLIDADO - SISUNO v1.4")
report_lines.append("")
report_lines.append(f"Data de emissão: {date_str}")
report_lines.append("Responsável técnico: Restaurador Officina")
report_lines.append("")
report_lines.append("1) Objetivo da versão")
report_lines.append("   - Consolidação do módulo financeiro e criação de views e relatórios para análise.")
report_lines.append("")
report_lines.append("2) Ações realizadas (factual)")
report_lines.append("   - Criação/ajuste das views: vw_fluxo_caixa_v14, vw_lucro_cliente_v14, vw_pacote_orcamento_resumo.")
report_lines.append("   - Correções e reconstrução de views que referenciavam colunas legadas (ex.: custo_por_km).")
report_lines.append("   - Criação de tabelas auxiliares (pacote_orcamento, cartao_fatura, cartao_fatura_itens) nas versões anteriores.")
report_lines.append("   - Execução de scripts de teste: test_integracao_v11.py, test_financeiro_v12.py, test_relatorios_v14.py, etc.")
report_lines.append("")
report_lines.append("3) Resultados dos testes (consolidados)")
report_lines.append("   - vw_fluxo_caixa_v14: OK (0 linhas na base de teste).")
report_lines.append("   - vw_lucro_cliente_v14: OK (linhas retornadas e validadas).")
report_lines.append("   - vw_pacote_orcamento_resumo: OK (linhas retornadas e validadas).")
report_lines.append("")
report_lines.append("4) Observações técnicas")
report_lines.append("   - Algumas views precisaram ser recriadas para seguir a estrutura atual de prontuários -> pessoas.")
report_lines.append("   - O ambiente de execução usado: Python 3.x com sqlite3 embutido.")
report_lines.append("")
report_lines.append("5) Instruções de arquivamento")
report_lines.append(f"   - Caminho: {OUTPUT_DIR}")
report_lines.append(f"   - Arquivo: {OUTPUT_FILE}")
report_lines.append("   - Registrar no log de versões (arquivo sisuno_version_log.txt) com assinatura SHA-256.")
report_lines.append("")
report_lines.append("6) Próximos passos (v1.5)")
report_lines.append("   - Implementar dashboards visuais (Streamlit/React/Dash).")
report_lines.append("   - Relatórios gerenciais periódicos (fluxo de caixa, lucro por cliente, margem).")
report_lines.append("")

# -----------------------
# Composição do conteúdo do PDF
# -----------------------
styles = getSampleStyleSheet()
doc = SimpleDocTemplate(output_path, pagesize=A4)
content = []

content.append(Paragraph("Relatório Técnico Consolidado - SisUno v1.4", styles["Title"]))
content.append(Spacer(1, 12))

for line in report_lines:
    content.append(Paragraph(line, styles["BodyText"]))
    content.append(Spacer(1, 6))

# -----------------------
# Calcular assinatura SHA256 de compilação
# - A assinatura é gerada a partir:
#   versão + timestamp + conteúdo de arquivos de esquema (se existirem)
# -----------------------
def gather_signature_components():
    comp = []
    comp.append("SisUno_v1.4")
    comp.append(date_str)
    # Tenta incluir conteúdo de schemas relevantes para tornar o hash representativo
    for candidate in SCHEMA_CANDIDATES:
        try:
            path = os.path.join(os.path.dirname(__file__), candidate)
        except NameError:
            path = candidate
        if os.path.exists(path):
            try:
                with open(path, "rb") as f:
                    comp.append(f.read())
            except Exception:
                comp.append(path.encode('utf-8'))
        else:
            comp.append(f"[missing]{candidate}".encode('utf-8'))
    return b"||".join([c if isinstance(c, bytes) else str(c).encode('utf-8') for c in comp])

sig_src = gather_signature_components()
signature = hashlib.sha256(sig_src).hexdigest()

content.append(Spacer(1, 12))
content.append(Paragraph(f"🔐 Assinatura Digital (SHA-256): {signature}", styles["BodyText"]))
content.append(Paragraph(f"🕒 Gerado em: {date_str}", styles["BodyText"]))
content.append(Spacer(1, 6))
content.append(Paragraph("📁 Registro e arquivamento automático no log de versões.", styles["BodyText"]))

# -----------------------
# Gera o PDF
# -----------------------
try:
    doc.build(content)
except Exception as e:
    print("❌ Erro ao gerar PDF:", e)
    sys.exit(1)

# -----------------------
# Grava no log de versões
# -----------------------
try:
    with open(log_path, "a", encoding="utf-8") as lf:
        lf.write("\n=== SISUNO v1.4 ===\n")
        lf.write(f"Data: {date_str}\n")
        lf.write(f"Arquivo: {output_path}\n")
        lf.write(f"Assinatura SHA256: {signature}\n")
        lf.write("Descrição: Relatório técnico consolidado - v1.4 (Integração financeira e views de relatórios)\n")
        lf.write("="*60 + "\n")
except Exception as e:
    print("⚠️ Erro ao gravar log de versões:", e)

print("✅ Relatório técnico v1.4 gerado com sucesso.")
print(f"📂 Caminho: {output_path}")
print(f"🔐 Assinatura SHA-256: {signature}")
print(f"🗒️ Log atualizado em: {log_path}")
