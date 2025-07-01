x = "1, 2, 3"
lst = x.split(',')
print(lst)

y = '&'.join(lst)
print(y)

z = ''.join(lst)
print(z)
z = ' and '.join(lst)
print(z)