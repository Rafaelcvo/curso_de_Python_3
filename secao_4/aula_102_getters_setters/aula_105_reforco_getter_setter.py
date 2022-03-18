"""
Revisao sobre getters e setters
Setter = configurando um valor (=)
Getter = obter um valor (.)
O getter pode ter sozinho no python, mas o setter não existe sem getter.

"""

class Pessoa:

    def __init__(self):
        self.atributo = 'inicial'
    @property
    def nome(self):
        return "Rafael Moreira"

    @nome.setter
    def nome(self, nome):
        self.atributo = nome


p1 = Pessoa()
print(p1.nome) # Assim a funcao se comporta como atributo.
print(p1.atributo)
print(p1.nome)