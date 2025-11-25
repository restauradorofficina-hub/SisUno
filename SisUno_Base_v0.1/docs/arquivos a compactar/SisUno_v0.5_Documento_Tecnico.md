🧾 Documento Técnico — SisUno v0.5

Projeto: Sistema de Gestão Integrado SisUno
Fase: Integração Cliente ↔ Prontuário
Data: 05/11/2025
Responsável: Restaurador Officina

🔹 1. Escopo da Versão v0.5

Esta versão tem como objetivo estabelecer o mecanismo de criação, armazenamento e vinculação automática de prontuários de clientes.
O sistema passa a organizar informações e documentos de forma estruturada, permitindo acompanhar o histórico de cada cliente e seus serviços.

🔹 2. Funcionalidades implementadas
🧩 Módulo de Prontuários

Objetivo: associar clientes a pastas físicas e registros digitais no banco de dados.

🔸 Operações principais:
Ação	Descrição
Criação automática de prontuário	Gera um diretório físico no caminho H:\SisUno\Clientes\<NOME>_<DATA>
Registro no banco de dados	Insere um registro em prontuarios com cliente_id, codigo, descricao, caminho, criado_em
Código identificador único	Formato: PRT-<id>-<timestamp>
Validação de cliente	Verifica se o cliente existe antes da criação do prontuário
Interface em terminal	Permite inserir dados de teste com prompts interativos (CLI)
🔹 3. Estrutura do banco de dados (atualizada)
📘 Tabela pessoas
Coluna	Tipo	Função
id	INTEGER	Identificador do cliente/fornecedor
tipo	TEXT	FÍSICA / JURÍDICA
nome	TEXT	Nome do cliente
papeis	TEXT	CLIENTE / FORNECEDOR / AMBOS
...	...	(demais campos de contato)
📘 Tabela prontuarios
Coluna	Tipo	Função
id	INTEGER	Identificador do prontuário
cliente_id	INTEGER	FK → pessoas.id
codigo	TEXT	Código único do prontuário
descricao	TEXT	Observação textual
caminho	TEXT	Caminho absoluto da pasta física
criado_em	DATETIME	Data e hora da criação
🔹 4. Scripts envolvidos
Arquivo	Localização	Função
add_prontuario.py	src/backend/	Criação do prontuário via CLI
schema_sisuno_v0.5.sql	database/	Estrutura completa do banco
inserir_cliente.py	database/	Script auxiliar para teste de clientes
test_orcamentos.py	database/	Próxima integração planejada
🔹 5. Caminho físico padrão
H:\SisUno\Clientes\<Nome>_<AAAA-MM-DD>\


Exemplo gerado:

H:\SisUno\Clientes\João_Silva_2025-11-05\

🔹 6. Status geral
Módulo	Situação	Observações
Estrutura base (v0.1)	✅ Concluído	Banco testado
Pessoas (clientes/fornecedores)	✅ Concluído	Suporta papel duplo
Prontuários	✅ Concluído	Integrado e funcional
Orçamentos	⏳ Em preparação	Aguardando link com prontuários
🔹 7. Próximos passos (Planejamento v0.6)

Criar relação entre prontuários e orçamentos (orcamentos.cliente_id → prontuarios.id).

Adicionar campos de status e andamento do serviço (ex: Em análise, Em execução, Concluído).

Iniciar gerador de orçamento básico em CLI.

Expandir para relatórios PDF (usando ReportLab).

🔹 8. Filosofia de projeto mantida

Estrutura modular, didática e expansível

Foco em uso local e intuitivo

Base preparada para futura interface web e mobile

📁 Caminho de armazenamento sugerido
H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\docs\SisUno_v0.5_Documento_Tecnico.md