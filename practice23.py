x = [1, 2]
y = [3, 4]
x.extend(y)
print(x)

lst = [1, 2]
lst1 = [1, 2]
lst2 = [3, 4]
lst.append([3, 4])  # [1, 2, [3, 4]] となる
print(lst)

print(lst1 + lst2)
