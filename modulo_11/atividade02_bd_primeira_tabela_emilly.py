import sqlite3

# 1. Conectar ao banco (ou criar se não existir)
conn = sqlite3.connect('atividade_info_cliente.db')
cursor = conn.cursor()

# 2. Criar a tabela (caso ainda não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# 3. Inserir dados iniciais
# Removi o executemany posterior para evitar erro de variável indefinida
clientes_dados = [
    ('Leticia Dorta', 'leticia.dorta@mail.com'),
    ('Ayla Sousa', 'ayla.sousa@mail.com'),
    ('Aurélio Dinis', 'aurelio.dinis@mail.com'),
    ('Igor Freitas', 'igor.freitas@mail.com'),
    ('Ana Cecília', 'ana.cecilia@mail.com'),
    ('Ana Alves', 'ana.alves@mail.com'),
    ('André Ramalho', 'andre.ramalho@mail.com'),
    ('Maria Helena', 'maria.helena@mail.com'),
    ('Antônio Fernandes', 'antonio.fernandes@mail.com'),
    ('Ana Clara Machado', 'ana.clara@mail.com'),
    ('Vitor Bispo Cruz', 'vitor.bispo@mail.com'),
    ('Pedro Henrique', 'pedro.henrique@mail.com')
]

cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', clientes_dados)
conn.commit()
print("Sucesso: Novos clientes inseridos.")

# --- CONSULTAR (Read) ---
print("\n--- LISTA DE CLIENTES ATUAIS ---")
cursor.execute("SELECT * FROM clientes")
for cliente in cursor.fetchall():
    print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

# --- ATUALIZAR (Update) ---
# Atualizando o e-mail do Igor Freitas para um formato específico
cursor.execute("UPDATE clientes SET email = ? WHERE nome = ?", ('igor.novo@email.com', 'Igor Freitas'))
print("\nSucesso: Email do Igor Freitas atualizado.")

# --- DELETAR (Delete) ---
# Deletando o registro da Leticia Dorta
cursor.execute("DELETE FROM clientes WHERE nome = ?", ('Leticia Dorta',))
print("Sucesso: Registro de Leticia Dorta removido.")

# Salvar alterações e fechar
conn.commit()
conn.close()

print("\nAtividade 2 concluída: Operações CRUD realizadas.")