🧩 SisUno — Documento Técnico v0.4
🔖 Versão

v0.4 — Módulo de Orçamentos Integrado aos Prontuários
Data: 04/11/2025
Autor: Equipe SisUno
Base anterior: v0.3 (Prontuário do Cliente)

🧭 1. Objetivo da versão

Introduzir o módulo de orçamentos, permitindo o registro completo de propostas comerciais e produtivas vinculadas ao prontuário do cliente.
Este módulo define a estrutura para controle de valores, itens, serviços e status de execução.

🧱 2. Estrutura Técnica
2.1 Tabelas adicionadas ao banco
Tabela: orcamentos
CREATE TABLE orcamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prontuario_id INTEGER NOT NULL,
    numero TEXT UNIQUE NOT NULL,
    data_emissao DATETIME DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT,
    valor_total REAL DEFAULT 0,
    status TEXT CHECK(status IN ('EM_NEGOCIACAO', 'APROVADO', 'CONCLUIDO', 'CANCELADO')) DEFAULT 'EM_NEGOCIACAO',
    observacoes TEXT,
    FOREIGN KEY (prontuario_id) REFERENCES prontuarios(id)
);

Tabela: orcamento_itens
CREATE TABLE orcamento_itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    orcamento_id INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    quantidade REAL DEFAULT 1,
    valor_unitario REAL DEFAULT 0,
    tipo TEXT CHECK(tipo IN ('PRODUTO', 'SERVICO', 'INSUMO')) DEFAULT 'SERVICO',
    subtotal REAL GENERATED ALWAYS AS (quantidade * valor_unitario) VIRTUAL,
    FOREIGN KEY (orcamento_id) REFERENCES orcamentos(id)
);

🔗 3. Relacionamentos
pessoas (1)───(n) prontuarios (1)───(n) orcamentos (1)───(n) orcamento_itens


Explicação:

Um cliente pode ter vários prontuários.

Cada prontuário pode ter vários orçamentos.

Cada orçamento contém vários itens (produtos, serviços, insumos).

⚙️ 4. Funcionalidades base
Função	Descrição	Estado
Criar orçamento	Gerar orçamento vinculado a um prontuário existente	✅ Implementado (estrutura SQL)
Adicionar itens	Inserir produtos, serviços e insumos	✅ Estrutura pronta
Calcular total	Soma automática dos subtotais (via SQL)	✅
Atualizar status	Controle do ciclo (negociação → aprovado → concluído)	🟡 Em desenvolvimento
Relatórios financeiros	Geração futura de relatórios consolidados	🔜 Planejado
🧪 5. Teste e validação sugeridos
Exemplo prático:

Inserir um orçamento vinculado ao prontuário:

INSERT INTO orcamentos (prontuario_id, numero, descricao, valor_total, status)
VALUES (1, 'ORC-0001', 'Restauração de cristaleira antiga', 0, 'EM_NEGOCIACAO');


Adicionar itens:

INSERT INTO orcamento_itens (orcamento_id, descricao, quantidade, valor_unitario, tipo)
VALUES
(1, 'Limpeza e lixamento', 1, 150.00, 'SERVICO'),
(1, 'Verniz especial', 2, 45.00, 'INSUMO'),
(1, 'Ferragem nova', 1, 80.00, 'PRODUTO');


Calcular o total:

SELECT SUM(subtotal) FROM orcamento_itens WHERE orcamento_id = 1;


Atualizar o valor total:

UPDATE orcamentos
SET valor_total = (SELECT SUM(subtotal) FROM orcamento_itens WHERE orcamento_id = 1)
WHERE id = 1;

📂 6. Localização de arquivos
Tipo	Caminho sugerido
Banco	database/sisuno_test.db
Scripts SQL	database/add_table_orcamentos.sql
Backend (futuro)	src/backend/orcamentos/
Relatórios	docs/relatorios/
🧠 7. Filosofia mantida

Clareza e organização visual: estrutura de orçamentos separada por cliente.

Escalabilidade modular: permite incluir etapas de aprovação, relatórios e faturamento.

Compatibilidade total: mantém integração com SQLite, Python e FastAPI (versões futuras).

🧾 8. Histórico de versões
Versão	Data	Alterações principais
v0.1	03/11/2025	Estrutura base e diretórios
v0.2	03/11/2025	Banco SQLite + modelo “pessoas” com múltiplos papéis
v0.3	04/11/2025	Módulo de prontuário do cliente
v0.4	04/11/2025	Módulo de orçamentos e itens implementado (base SQL)

📄 Documento gerado automaticamente — SisUno v0.4 (fase estrutural finalizada)