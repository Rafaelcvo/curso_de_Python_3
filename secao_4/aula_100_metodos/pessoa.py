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


p1 = Pessoa('Luiz', 32)
print(p1.idade)
p1.get_ano_nascimento()
p = Pessoa.por_ano_nascimento('Luiz', 1990)

# p2 = Pessoa('Antonio', 1950)
# print(Pessoa.ano_atual)
# p2.get_ano_nascimento()
