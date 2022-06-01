import math

PI = math.pi

def dobre_valor(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


if __name__ == '__main__':
    lista = [1,2,3,4,5]
    print(dobre_valor(lista))
    print(multiplica(lista))
    print(PI)
    print(__name__)