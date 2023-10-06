a = b = c = [1, 2, 3]
print(a, b, c)
print(id(a), id(b), id(c))
a.append(4)
print(a, b, c)
print(id(a), id(b), id(c))

print('-----------------------------')

x = 10
y = 10
print(id(x), id(y))
y = y + 123456789011 - 123456789011
print(id(x), id(y))
