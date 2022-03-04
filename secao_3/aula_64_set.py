s1 = set()

s1.add(2)
s1.add(('luiz', 'antonio', 'rafael'))

print(s1)

s1 = {1,2,3,4,5}
s2 = {2,3,5,6,7}

s3 = s1 | s2

print(s3)
print(s1-s2)
print(s1 & s2)
print(s1  s2)
