def teste(nome='Rafael', msg='Olá'):
    print(msg, nome)


teste('Joao', 'Bem Vindo')


def func(*args, **nomes):
    print(args)
    print(nomes)


lista = [1,2,3,4,5]
lista2 = [10,20,30]
func(*lista, *lista2, nome='Luiz', sobrenome='Alves')