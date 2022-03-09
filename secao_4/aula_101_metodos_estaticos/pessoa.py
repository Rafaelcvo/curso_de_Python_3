from random import randint
from datetime import datetime

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        hora_atual = datetime.now()
        return rand, hora_atual



p1 = Pessoa('Luiz', 32)
print(p1.idade)
p1.get_ano_nascimento()
p = Pessoa.por_ano_nascimento('Luiz', 1990)
print(Pessoa.gera_id())
print(p1.gera_id())

