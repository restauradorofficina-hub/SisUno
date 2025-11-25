from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

# Caminho do PDF
output_path = r"H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\docs\Relatorios_Tecnicos\Relatorio_Tecnico_SisUno_v0.7.pdf"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Estilos
styles = getSampleStyleSheet()
title = styles["Title"]
subtitle = styles["Heading2"]
body = styles["BodyText"]

# Documento
doc = SimpleDocTemplate(output_path, pagesize=A4)
story = []

# Cabeçalho
story.append(Paragraph("Relatório Técnico — SisUno v0.7 (Marco de Consolidação)", title))
story.append(Spacer(1, 20))

# 1. Identificação
story.append(Paragraph("1. Identificação do Projeto", subtitle))
story.append(Paragraph(f"""
<b>Nome:</b> SisUno — Sistema Integrado de Gestão de Serviços, Produção e Vendas<br/>
<b>Responsável Técnico:</b> Restaurador Officina<br/>
<b>Versão:</b> 0.7 (Marco de Integração)<br/>
<b>Data:</b> {datetime.now().strftime("%d/%m/%Y %H:%M")}<br/>
<b>Finalidade:</b> Consolidar a base funcional e integrar os módulos de cálculo de custos operacionais e deslocamento.
""", body))
story.append(Spacer(1, 12))

# 2. Estrutura Atual
story.append(Paragraph("2. Estrutura Atual do Sistema", subtitle))
story.append(Paragraph("""
O SisUno encontra-se estável até a versão 0.6.2, com os seguintes módulos validados:<br/>
- Pessoas: cadastro unificado de clientes e fornecedores.<br/>
- Prontuários: criação automática de pastas por cliente/projeto.<br/>
- Orçamentos: geração e exportação em PDF.<br/>
- Financeiro: estrutura inicial de lançamentos e débitos/créditos.<br/>
- Gerador de PDFs: automação de relatórios técnicos.<br/>
- Estrutura de diretórios: padronizada e validada no ambiente Windows 11.
""", body))
story.append(Spacer(1, 12))

# 3. Novas Integrações
story.append(Paragraph("3. Novas Integrações (v0.7)", subtitle))
story.append(Paragraph("""
Foram incorporadas duas planilhas de apoio operacional que ampliam a precisão dos cálculos:<br/><br/>
1. Planilha de Custos Operacionais — define custos de mão de obra, encargos e despesas fixas.<br/>
2. Planilha de Deslocamento — calcula o custo real por quilômetro rodado (COE, COT e remuneração).<br/><br/>
Essas planilhas servirão de base para o módulo de cálculo automático de orçamentos.
""", body))
story.append(Spacer(1, 12))

# 4. Planejamento de Integração
story.append(Paragraph("4. Planejamento de Integração (v0.7.1)", subtitle))
story.append(Paragraph("""
A próxima etapa visa converter as planilhas em tabelas SQL integradas:<br/>
- Tabela custos_operacionais (salários, encargos, despesas fixas).<br/>
- Tabela veiculos_deslocamento (dados de custo por km, manutenção, consumo).<br/>
- Adaptação do módulo Orçamentos para aplicar ambos os cálculos.<br/>
- Geração automática de relatórios financeiros consolidados.
""", body))
story.append(Spacer(1, 12))

# 5. Próximas Etapas
story.append(Paragraph("5. Próximas Etapas (v0.8 e além)", subtitle))
story.append(Paragraph("""
- Criação da interface gráfica do módulo de orçamentos.<br/>
- Implementação de relatórios dinâmicos e dashboards financeiros.<br/>
- Backup automático do banco de dados.<br/>
- Exportação para Excel e histórico de versões.<br/>
- Planejamento de migração para PostgreSQL (multiusuário).<br/>
""", body))
story.append(Spacer(1, 12))

# 6. Conclusão Técnica
story.append(Paragraph("6. Conclusão Técnica", subtitle))
story.append(Paragraph("""
O SisUno atinge maturidade estrutural suficiente para expansão e automação de cálculos.<br/>
Os módulos estão estáveis e integrados, e a documentação técnica está consolidada.<br/><br/>
<b>Status atual:</b> 65% do núcleo concluído e validado.<br/>
<b>Próximo marco:</b> v0.7.1 — automação dos cálculos e atualização do banco de dados.
""", body))
story.append(Spacer(1, 12))

# 7. Instruções de Arquivamento
story.append(Paragraph("7. Instruções de Arquivamento e Versionamento", subtitle))
story.append(Paragraph("""
O arquivo deste relatório deve ser armazenado na pasta:<br/>
<code>docs/Relatorios_Tecnicos/</code><br/><br/>
O padrão de nomenclatura para controle de versões técnicas é:<br/>
<code>Relatorio_Tecnico_SisUno_vX.X.pdf</code><br/><br/>
Cada nova versão deverá incluir:<br/>
- Histórico de alterações técnicas.<br/>
- Descrição das integrações realizadas.<br/>
- Registro de validações e testes executados.
""", body))

# Geração do PDF
doc.build(story)

print(f"✅ Relatório técnico gerado com sucesso!\n📁 Caminho: {output_path}")
