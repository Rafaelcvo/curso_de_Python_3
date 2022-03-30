"""
rszalski.github.io/magicmethods
"""

class A:
    def __new__(cls, *args, **kwargs):
        print("I am New")
        cls.nome = "Rafael"
        return object.__new__(cls)

    def __init__(self):
        print("I am Init")

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def fala_oi(self):
        print('Oi')

    def __setattr__(self, key, value):
        print(key, value)



a = A()
a(1,2,3,4,5, nome='Rafael')
a.fala_oi()
a.nome = 'Rafael Moreira'