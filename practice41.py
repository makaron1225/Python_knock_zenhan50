dct = {"id": "0001", "name": "guest"}
dct["key"] = "value"
print(dct)
print(dct["name"])
print(dct["id"], dct["name"], dct["key"])

dct = {"name": "0001", "name": "guest"}  # name が重複している
print(dct)  # {'name': 'guest'} が表示される
