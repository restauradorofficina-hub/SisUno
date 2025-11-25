🧾 Documento Técnico — SisUno v0.6

Projeto: Sistema de Gestão Integrado SisUno
Fase: Integração Prontuário ↔ Orçamentos
Data: 05/11/2025
Responsável: Restaurador Officina

🔹 1. Escopo da Versão v0.6

Esta versão visa criar e vincular orçamentos diretamente aos prontuários, centralizando todas as informações financeiras, materiais e de serviço em um ponto único de controle.

Cada orçamento passa a ser:

vinculado a um cliente (via prontuário),

conter itens e serviços detalhados,

possuir status de andamento (ex: em elaboração, em aprovação, aprovado, em execução, concluído).

🔹 2. Estrutura lógica prevista
📘 Tabela orcamentos
Campo	Tipo	Descrição
id	INTEGER	Identificador único
prontuario_id	INTEGER	FK → prontuarios.id
codigo	TEXT	Código interno (formato: ORC-<id>-<timestamp>)
descricao	TEXT	Breve identificação do orçamento
valor_total	REAL	Valor total calculado (somatório dos itens)
status	TEXT	[“EM_ELABORACAO”, “APROVADO”, “CANCELADO”, “CONCLUIDO”]
criado_em	DATETIME	Registro de criação
atualizado_em	DATETIME	Última modificação
📘 Tabela orcamento_itens
Campo	Tipo	Descrição
id	INTEGER	Identificador do item
orcamento_id	INTEGER	FK → orcamentos.id
tipo_item	TEXT	["PRODUTO", "SERVICO", "INSUMO"]
descricao	TEXT	Detalhe do item
quantidade	REAL	Quantidade estimada
valor_unitario	REAL	Valor de cada unidade
valor_total	REAL	Quantidade × Valor unitário
observacao	TEXT	Comentários adicionais
🔹 3. Integração com os módulos existentes
Módulo	Relacionamento	Tipo de vínculo
pessoas	Cliente ↔ prontuário	1:N
prontuarios	Prontuário ↔ orçamento	1:N
orcamentos	Orçamento ↔ itens	1:N
🔹 4. Operações previstas
Operação	Descrição
criar_orcamento()	Gera um novo orçamento vinculado a um prontuário existente
adicionar_item()	Inclui produto, serviço ou insumo ao orçamento
atualizar_valor_total()	Soma automática dos itens e atualiza o campo valor_total
listar_orcamentos_cliente()	Mostra todos os orçamentos do cliente
atualizar_status()	Altera o estado do orçamento conforme o fluxo
🔹 5. Scripts previstos (v0.6)
Arquivo	Localização	Função
add_orcamento.py	src/backend/	Cria orçamentos vinculados a prontuários
add_item_orcamento.py	src/backend/	Adiciona itens ao orçamento
test_orcamentos_v06.py	database/	Valida a estrutura e relações
update_schema_v06.sql	database/	Criação das novas tabelas orcamentos e orcamento_itens
🔹 6. Fluxo de uso prático (terminal / CLI)

1️⃣ Criar ou localizar cliente
2️⃣ Criar prontuário
3️⃣ Gerar orçamento vinculado ao prontuário
4️⃣ Inserir itens (produtos e serviços)
5️⃣ Fechar ou aprovar orçamento

🔹 7. Projeção futura (v0.7+)

Geração de PDF de orçamento para envio ao cliente

Controle de etapas de execução e custos reais

Relatórios analíticos financeiros e de produção

🔹 8. Local sugerido de armazenamento
H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\docs\SisUno_v0.6_Documento_Tecnico.m