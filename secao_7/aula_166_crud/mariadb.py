import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        db = 'clientes',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()


def insere():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = "INSERT INTO clientes(nome, sobrenome, idade, peso) " \
                  "VALUES(%s, %s, %s, %s)"
            dados = [
                ('David', 'Ferreira', 9, 78),
                ('Antonio', 'Augusto', 19, 48)
            ]
            cursor.executemany(sql, dados)
            conexao.commit()

def select():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = "SELECT * FROM clientes;"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            for l in resultado:
                print(l)

def update(id, nome):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = "UPDATE clientes SET nome=%s WHERE id = %s"
            cursor.execute(sql, (nome, id,))
            conexao.commit()


def delete(id):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = f"DELETE FROM clientes WHERE id = %s;"
            cursor.execute(sql, (id,))
            conexao.commit()

# insere()
# delete(11)
update(2, 'Rafael')
select()