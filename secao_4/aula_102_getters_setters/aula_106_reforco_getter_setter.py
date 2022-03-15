"""
Revisao sobre getters e setters
Setter = configurando um valor (=)
Getter = obter um valor (.)
O getter pode ter sozinho no python, mas o setter não existe sem getter.

"""

class Pessoa:

    def __init__(self, nome):
        self._nome = nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('Setter foi executado')
        nome += ' Moreira'
        self._nome = nome

    @property
    def sobrenome(self):
        return 'Sobrenome'


p1 = Pessoa('Rafael')
print(p1._nome) # Assim a funcao se comporta como atributo.
print(p1.sobrenome)