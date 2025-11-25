-- Corrige estrutura da tabela custos_base (adiciona atualizado_em)
ALTER TABLE custos_base ADD COLUMN atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP;
