"""
Encapsulamento
public, protected, private
_ private ou protected mais fraco
__ private mais forte0000
"""
class BaseDados:
    def __init__(self):
        self.__dados ={}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f"{id} - {nome}")

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDados()

bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')

bd.apagar_cliente(2)
bd.lista_clientes()
bd.__dados = 'Vai dar erro'
print(bd.__dados)
print(bd._BaseDados__dados)
bd.inserir_cliente(4, 'Ronaldo')
bd.lista_clientes()

