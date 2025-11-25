from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from datetime import datetime
import hashlib
import os

# ==============================
# 📄 CONFIGURAÇÕES INICIAIS
# ==============================
output_dir = r"H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\docs\Relatorios_Tecnicos"
output_path = os.path.join(output_dir, "Diario_Engenharia_SisUno_v1.3.pdf")
log_file = os.path.join(output_dir, "sisuno_version_log.txt")

# ==============================
# 📋 CONTEÚDO DO DIÁRIO
# ==============================
diario_text = """
========================================
DIÁRIO DE ENGENHARIA – SISUNO v1.3
========================================
📅 Data de emissão: {data}
🧑‍💻 Responsável: Officina – Desenvolvimento e Integração de Sistemas
📁 Diretório: {path}
========================================

1️⃣ CONTEXTO GERAL
----------------------------------------
A versão v1.3 do SisUno marca a consolidação financeira do sistema,
introduzindo o controle de pacotes de orçamentos e a gestão de faturas
de cartão de crédito.

Durante o desenvolvimento, foi dada ênfase à correção das dependências
entre as views `vw_orcamentos_com_custos`, `vw_resumo_financeiro` e `vw_faturas_cartao_resumo`.

Foram enfrentadas e solucionadas inconsistências herdadas de versões
anteriores (v1.0–v1.2), principalmente nas referências a colunas e
na estrutura das tabelas auxiliares.

----------------------------------------
2️⃣ OCORRÊNCIAS TÉCNICAS REGISTRADAS
----------------------------------------
🔹 *Erro: `no such column: cv.custo_por_km`*
   – Causa: ausência do campo na view durante reconstrução parcial.
   – Ação: recriação completa da view com JOIN explícito em `custos_veiculo`.

🔹 *Erro: `no such table: financeiro_antigo`*
   – Causa: referência residual na view `vw_resumo_financeiro`.
   – Ação: limpeza e substituição da view; estrutura corrigida
     via script `fix_table_financeiro_v11.sql`.

🔹 *Erro: `id_orcamento` ausente em financeiro*
   – Causa: coluna não sincronizada na reconstrução.
   – Ação: adição manual por script Python; verificação confirmada via PRAGMA.

🔹 *Problemas de identação em Python interativo*
   – Causa: tentativas de execução no REPL (prompt interativo).
   – Ação: orientação para salvar scripts `.py` e executar pelo terminal.

----------------------------------------
3️⃣ AJUSTES E MELHORIAS IMPLEMENTADAS
----------------------------------------
✅ Criação da tabela `pacote_orcamento` e `pacote_orcamento_itens`
   – Permite consolidar múltiplos orçamentos em um único cliente.

✅ Criação das tabelas `cartao_fatura` e `cartao_fatura_itens`
   – Estruturação de controle financeiro detalhado.

✅ Revisão completa das views financeiras:
   – `vw_orcamentos_com_custos`
   – `vw_resumo_financeiro`
   – `vw_faturas_cartao_resumo`

✅ Geração do módulo de teste `test_financeiro_v12.py`
   – Garantia de consistência e automatização de validação.

----------------------------------------
4️⃣ RESULTADOS ALCANÇADOS
----------------------------------------
📊 As tabelas e views estão funcionando de forma integrada.
💰 As faturas são consolidadas corretamente por cartão.
📦 Os pacotes de orçamento vinculam-se automaticamente aos clientes.
🔗 As relações de chave estrangeira entre financeiro e orçamentos
foram testadas e validadas com sucesso.
🧩 O sistema encontra-se pronto para geração de relatórios
gerenciais e dashboards (versão 1.4).

----------------------------------------
5️⃣ PRÓXIMOS PASSOS (Planejamento v1.4)
----------------------------------------
🔸 Implementação de *Relatórios Gerenciais* automáticos em PDF.
🔸 Introdução do *Painel Financeiro Consolidado* (interface visual).
🔸 Integração com módulo de controle de fluxo de caixa.
🔸 Definição de indicadores de margem, custos e lucro operacional.
🔸 Estruturação da camada de segurança de dados (usuários e perfis).

----------------------------------------
6️⃣ INSTRUÇÕES DE ARQUIVAMENTO
----------------------------------------
📂 Diretório:
H:\\Reserva\\Pessoal\\Sistema vendas e orçamento\\SisUno_Base_v0.1\\docs\\Relatorios_Tecnicos\\
📄 Nome do arquivo:
Diario_Engenharia_SisUno_v1.3.pdf

----------------------------------------
🔖 Observações finais:
Este documento deve ser arquivado junto ao relatório técnico v1.3,
sendo referência para auditoria, rastreabilidade e versionamento.
========================================
"""

# ==============================
# 🧾 GERAÇÃO DO PDF
# ==============================
styles = getSampleStyleSheet()
doc = SimpleDocTemplate(output_path, pagesize=A4)
content = [
    Paragraph("DIÁRIO DE ENGENHARIA – SISUNO v1.3", styles["Title"]),
    Spacer(1, 12),
    Paragraph(diario_text.format(data=datetime.now().strftime("%Y-%m-%d %H:%M"), path=output_path), styles["BodyText"]),
    PageBreak()
]

# Assinatura digital
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
signature = hashlib.sha256(f"Diario_v1.3_{timestamp}".encode()).hexdigest()

content.append(Spacer(1, 12))
content.append(Paragraph(f"🔐 Assinatura Digital: {signature}", styles["BodyText"]))
content.append(Paragraph(f"🕒 Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", styles["BodyText"]))
content.append(Paragraph(f"📎 Documento de acompanhamento técnico – v1.3", styles["BodyText"]))

doc.build(content)

# Registro no log
with open(log_file, "a", encoding="utf-8") as f:
    f.write(f"\n=== Diário de Engenharia v1.3 ===\n")
    f.write(f"Data: {datetime.now()}\n")
    f.write(f"Arquivo: {output_path}\n")
    f.write(f"Assinatura: {signature}\n")
    f.write(f"Descrição: Registro técnico da versão 1.3 - Consolidação financeira.\n")
    f.write("="*50 + "\n")

print("✅ Diário de Engenharia v1.3 gerado com sucesso!")
print(f"📂 Caminho: {output_path}")
print(f"🔐 Assinatura: {signature}")
