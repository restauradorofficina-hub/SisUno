# RELATÓRIO TÉCNICO INICIAL — SISUNO v1.5
**Módulo**: Relatórios Executivos e Painel Financeiro (Dashboard)  
**Data:** (preencher)  
**Responsável:** Restaurador Officina

## 1. Objetivo
Implementar relatórios executivos e um dashboard interativo que permitam:
- visão consolidada do fluxo de caixa (mensal);
- análise de faturas de cartão (por cartão, por mês, status);
- lucro estimado por cliente / por serviço;
- indicadores-chave (KPIs): receita total, despesa total, margem média, faturas em aberto.

## 2. Escopo funcional
- Views SQL agregadas (mensal, por cliente, por pacote).
- Scripts de geração automática de PDF (executivo) usando ReportLab / Pandas.
- Dashboard interativo (Streamlit) com filtros por período, cliente, cartão e status.
- Testes automatizados que validem views e geração de relatórios.

## 3. Estrutura proposta (arquivos)
- database/
  - vw_resumo_mensal_v15.sql
  - vw_kpis_v15.sql
  - vw_cliente_detalhado_v15.sql
  - update_database_v15.py
  - test_relatorios_v15.py
- src/backend/
  - gerar_relatorio_executivo_v15.py
- src/dashboard/
  - dashboard_streamlit_v15.py
- docs/Relatorios_Tecnicos/
  - Relatorio_Tecnico_SisUno_v1.5.md (este arquivo)
  - gerar_relatorio_v15_helper.py (opcional)

## 4. Requisitos / Dependências
- Python 3.10+ (64-bit recomendado)
- Bibliotecas: pandas, reportlab, matplotlib, streamlit, sqlite3 (embutido)
- Instalação (exemplo):
