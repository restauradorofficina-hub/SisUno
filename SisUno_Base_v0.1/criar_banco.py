import sqlite3, os
from pathlib import Path

db_path = Path(r"H:\Reserva\Pessoal\Sistema vendas e orçamento\SisUno_Base_v0.1\database\sisuno_test.db")

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute('''CREATE TABLE pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    endereco TEXT,
    cidade TEXT,
    uf TEXT,
    data_cadastro TEXT DEFAULT (datetime('now'))
)''')

c.execute('''CREATE TABLE prontuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    codigo TEXT,
    caminho TEXT,
    descricao TEXT,
    data_criacao TEXT,
    FOREIGN KEY (cliente_id) REFERENCES pessoas (id)
)''')

c.execute("INSERT INTO pessoas (nome, telefone, cidade, uf) VALUES ('João Silva', '11 99999-9999', 'São Paulo', 'SP')")
c.execute("INSERT INTO pessoas (nome, telefone, cidade, uf) VALUES ('Maria Oliveira', '21 98888-7777', 'Rio de Janeiro', 'RJ')")

conn.commit()
conn.close()
print("BANCO CRIADO COM SUCESSO!")
os.startfile(str(db_path.parent))