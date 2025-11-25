-- =========================================
-- 🧩 SISUNO v0.7 - Atualização da tabela ORCAMENTOS
-- Adiciona suporte para geração e registro de PDFs
-- =========================================

PRAGMA foreign_keys = OFF;

-- Verificar e adicionar a coluna arquivo_pdf se ainda não existir
ALTER TABLE orcamentos ADD COLUMN arquivo_pdf TEXT;

-- Atualizar registros existentes com valor nulo
UPDATE orcamentos SET arquivo_pdf = NULL WHERE arquivo_pdf IS NULL;

PRAGMA foreign_keys = ON;

-- Registrar atualização no log financeiro (opcional)
INSERT INTO financeiro (descricao, valor, criado_em)
VALUES ('Atualização v0.7 - Adição de suporte a PDF em orçamentos', 0, CURRENT_TIMESTAMP);

-- =========================================
-- ✅ Atualização concluída - SisUno v0.7
-- =========================================

