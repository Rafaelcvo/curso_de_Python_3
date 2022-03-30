class A:
    def divid(n1, n2):
        try:
            return n1/n2
        except ZeroDivisionError as erro:
            print("Imposivel dividir")
            raise
    try:
        print(divid(4,0))
    except:
        print('erro')

class B:
    def divide(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        if self.n2 == 0:
            raise ValueError('n2 nao pode ser zero')
        return self.n1 / self.n2

a = B()
print(a.divide(2,0))