-- add_columns_financeiro_v13.sql
PRAGMA foreign_keys = OFF;

-- adiciona coluna para vincular lançamentos à fatura do cartão
ALTER TABLE financeiro ADD COLUMN id_fatura INTEGER;

-- adiciona controle de pagamento
ALTER TABLE financeiro ADD COLUMN status_pagamento TEXT DEFAULT 'pendente';
ALTER TABLE financeiro ADD COLUMN data_pagamento DATETIME;

PRAGMA foreign_keys = ON;
