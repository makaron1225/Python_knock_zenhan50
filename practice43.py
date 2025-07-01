even_lst = [x + 1 for x in range(1, 10) if x % 2]
print(even_lst)

even_lst = [x for x in range(1, 11) if x % 2 == 0]
print(even_lst)

odd_lst = [x for x in range(1, 11) if x % 2 != 0]
print(odd_lst)

even_list = []
for x in range(1, 11):
    if x % 2 == 0:
        even_list.append(x)
print(even_list)

even_list = [2 * x for x in range(1, 6)]
print(even_list)

