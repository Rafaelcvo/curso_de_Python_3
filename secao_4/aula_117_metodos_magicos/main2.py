class B:

    def __init__(self):
        pass

    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'Voce nao pode fazer isto'
        else:
            self.__dict__[key] = value

    def __del__(self):
        print('Objeto coletado')

    def __str__(self):
        return 'Essa é minha classe'

    def __len__(self):
        return 60

a = B()
a.nome = 'Rafael'
print(a.nome)
a.sobrenome = 'Costa'
print(a.sobrenome)
print(len(a))