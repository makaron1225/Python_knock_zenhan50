x = -1
if x < 0:
    try:
        raise ValueError("負の値が入力されました")
    except ValueError as error:
        print(error)


x = -1
if x < 0:
    raise ValueError("負の値が入力されました")
