import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Augusto', 70.6))
# # outra maneira de evitar sqlinjection
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Antonio', 'peso': 50.6})
# # outra maneira
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome': 'Rafael', 'peso': 90.5})
# conexao.commit()

# cursor.execute('UPDATE clientes SET nome = :nome WHERE id=:id', {'nome': 'Joanna', 'id': 2})
# cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 1})

conexao.commit()
# cursor.execute('SELECT nome, peso FROM  clientes WHERE peso > :peso', {'peso': 80})
cursor.execute('SELECT * FROM  clientes')

for linha in cursor.fetchall():
    ident, nome, peso = linha
    print(ident, nome, peso)
    # nome, peso = linha
    # print(f'Nome: {nome} e peso: {peso}')

cursor.close()
conexao.close()