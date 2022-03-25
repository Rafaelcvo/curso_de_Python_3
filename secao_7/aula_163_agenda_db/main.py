import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inser(self, nome, telefone):
        query = 'INSERT INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(query, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        query = 'UPDATE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(query, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        query = 'DELETE FROM agenda id=?'
        self.cursor.execute(query, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for l in self.cursor.fetchall():
            print(l)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaDB('basedados.db')
    agenda.inser('Rafael', '11111')