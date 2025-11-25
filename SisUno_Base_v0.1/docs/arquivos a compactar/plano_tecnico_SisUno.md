📘 Conteúdo completo do arquivo plano_tecnico_SisUno.md
# ⚙️ Plano Técnico – Projeto SisUno

## 💻 Arquitetura Geral
O SisUno será desenvolvido em **modo híbrido**, combinando:
- operação local (banco e interface no computador);
- base pronta para versão web futura (API e interface React).

### 🔹 Camadas
1. **Banco de dados:** SQLite local, com estrutura compatível com PostgreSQL.
2. **Camada lógica:** Python (FastAPI) – responsável por regras de negócio e API local.
3. **Interface:** React (modo desktop/web) – exibe as telas de uso.
4. **Relatórios:** Gerados em PDF e Excel via módulos integrados.
5. **Armazenamento:** Arquivos locais + sincronização futura com nuvem.

---

## 🧱 Estrutura de diretórios


SisUno/
├── docs/ → documentação e guias
├── database/ → scripts e estrutura do banco
├── src/ → código-fonte (backend e frontend)
├── design/ → identidade visual e protótipos
└── archive/ → versões e histórico


---

## 🧩 Tecnologias sugeridas
| Camada | Tecnologia | Justificativa |
|---------|-------------|----------------|
| Banco | SQLite / PostgreSQL | leve e escalável |
| Backend | Python + FastAPI | simples, estável, multiplataforma |
| Frontend | React.js | interface moderna e responsiva |
| Relatórios | Python (ReportLab, Pandas) | geração nativa de PDFs e planilhas |
| Versões futuras | Flutter ou PWA | suporte mobile e web |

---

## 🧰 Ferramentas de suporte
- **GitHub** – controle de versões do código  
- **Google Drive** – armazenamento documental e histórico  
- **VS Code** – editor de código recomendado  
- **Python 3.12+** – motor principal local  
- **Node.js 20+** – suporte à interface React  

---

## 🧠 Filosofia técnica
- Estrutura modular e expansível  
- Simplicidade de instalação (executável único local)  
- Sem dependência de internet  
- Futuro suporte web e mobile sem reescrever código  

---

📄 **Documento gerado automaticamente — versão 1.0 (base técnica)**