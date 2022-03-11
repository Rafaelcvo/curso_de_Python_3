class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual /100))

    # Getter
    @property
    def preco(self):
        return self._preco #(o nome pode ser qualquer um, mas por conversão usa _preco que faz referencia self.preco )

    # Setter
    @preco.setter
    def preco(self, valor):
        self._preco = valor
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


p1 = Produto('CAMISA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('Caneca', 'R$5')
p2.desconto(10)
print(p2.nome, p2.preco)
