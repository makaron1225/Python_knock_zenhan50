st = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for s in st:
    print(s)

print(1 in st)
print(88 in st)

lst = [1, 1, 2, 3]
st = set(lst)  # 集合に変換、重複要素 1 が削除される
print(st)
print(type(st))

st = {1, 2, 3}
lst = list(st)  # リストに変換
lst.append(1)  # 末尾に重複要素 1 を追加する
print(lst)
print(type(lst))
