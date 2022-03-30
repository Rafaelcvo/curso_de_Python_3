try:
    a = 1/0
except NameError as erro:
    print('Houve erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice.')
except Exception as erro:
    print('Erro inesperado:', erro)
else:
    print('Seu bloco foi executado')
    print(a)
finally:
    print('Finalmente.')

print('Cotinua')