class A:
    vc = 123

    def __init__(self):
        self.vc = 444

a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)

A.vc = 555
a2 = A()
a2.vc = 888

print(a2.vc)
print(A.vc)
print(a2.__dict__)
print(A.__dict__)