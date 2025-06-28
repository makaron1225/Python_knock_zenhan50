x = print("print 関数の戻り値を取得します")
if x is None:
    print("print 関数の戻り値は None です")

y = print(12)
if y is None:
    print("print 関数の戻り値は None です")

# Pythonにおいてprintは画面に文字を表示する役割
# しか持たないため、戻り値は例外なくNoneとなる。
