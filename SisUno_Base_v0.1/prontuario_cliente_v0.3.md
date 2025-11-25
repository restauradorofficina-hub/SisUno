🧾 Conteúdo completo (copie e cole no Bloco de Notas, salve em UTF-8)
# 🧩 SisUno – Documento Técnico Complementar  
## Módulo: Prontuário do Cliente  
### Versão: v0.3 – Núcleo de Cliente  
📅 Data: 2025-11-01  

---

## 📖 Visão Geral
O **Prontuário do Cliente** é o núcleo de registro e histórico do sistema **SisUno**.  
Ele integra informações cadastrais, arquivos físicos e dados operacionais em um único ponto de acesso.

O modelo reflete a prática atual do negócio: cada cliente possui uma **pasta física** no sistema de arquivos do Windows, onde são armazenados todos os elementos do seu projeto — fotos, documentos, orçamentos, relatórios e arquivos de projeto (ex: SketchUp).

O SisUno organiza e referencia automaticamente essas pastas, mantendo o controle e histórico de forma centralizada.

---

## 🧱 Estrutura Geral



/SisUno/Clientes/
├── João_Silva_2025-11-01/
│ ├── fotos/
│ ├── orcamentos/
│ ├── documentos/
│ ├── sketchup/
│ └── notas.txt
├── Maria_Alves_2025-11-01/
│ ├── fotos/
│ ├── orcamentos/
│ └── ...


Cada pasta de cliente corresponde a **um registro na tabela `prontuarios`**.

---

## 🗄️ Estrutura de Banco de Dados

### 🔹 Tabela: `prontuarios`
```sql
CREATE TABLE prontuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pessoa INTEGER NOT NULL,
    codigo TEXT UNIQUE,
    descricao TEXT,
    caminho_pasta TEXT,
    data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('ABERTO', 'FECHADO', 'ARQUIVADO')) DEFAULT 'ABERTO',
    observacoes TEXT,
    FOREIGN KEY (id_pessoa) REFERENCES pessoas(id)
);

🔗 Relacionamentos Principais
Tabela	Relacionamento	Descrição
pessoas	1:N → prontuarios	Cada pessoa pode ter vários prontuários
prontuarios	1:N → orcamentos	Cada prontuário pode ter vários orçamentos
orcamentos	1:N → financeiro	Cada orçamento pode gerar lançamentos financeiros
⚙️ Funcionalidade Operacional
Etapa	Ação	Efeito
1. Criação de cliente	O sistema cria o registro na tabela pessoas	Cadastro básico
2. Abertura de prontuário	Gera um novo registro em prontuarios e cria uma pasta física no disco	Pasta vinculada ao cliente
3. Registro de orçamentos e serviços	Associados ao prontuário via id_prontuario	Histórico completo
4. Armazenamento de arquivos	Fotos, relatórios e projetos salvos manualmente ou via upload	Organização automática por subpastas
5. Encerramento	Status do prontuário muda para FECHADO ou ARQUIVADO	Histórico mantido, edição bloqueada
📂 Estrutura Física Recomendada

Padrão de diretórios sugerido (configurável no futuro via painel do sistema):

H:\SisUno\Clientes\
    └── {Nome_Cliente}_{Data_Abertura}\
        ├── fotos\
        ├── orcamentos\
        ├── documentos\
        ├── sketchup\
        └── notas.txt


O campo caminho_pasta do banco armazena o endereço completo desta pasta,
permitindo acesso direto pelo sistema com um clique.

🧠 Benefícios da Integração

Centralização: Todos os dados e documentos do cliente em um único ponto.

Flexibilidade: Arquivos continuam acessíveis fora do sistema.

Rastreabilidade: Cada documento vinculado a um prontuário.

Escalabilidade: Possibilidade futura de sincronização com nuvem (Google Drive ou Nextcloud).

Segurança: Separação física e lógica dos dados de cada cliente.