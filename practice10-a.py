# エスケープシーケンスの出力例
print("キャリッジリターン: Hello\rWorld")  # \r → 行頭に戻る
print("改行: Hello\nWorld")  # \n → 改行
print("タブ: Hello\tWorld")  # \t → タブ
print("バックスペース: Hello\bWorld")  # \b → 1文字削除
print("フォームフィード: Hello\fWorld")  # \f → 一部の環境でページ送り
print("垂直タブ: Hello\vWorld")  # \v → 垂直タブ（環境によって表示が異なる）
print("バックスラッシュ: C:\\test")  # \\ → バックスラッシュそのまま表示
print("シングルクォート: It\'s Python")  # \' → シングルクォート
print("ダブルクォート: She said \"Hello\"")  # \" → ダブルクォート
print("16進数コード: \x41\x42\x43")  # \xhh → A B C
print("8進数コード: \101")  # \101 は 'A'（8進数）
print("Unicode: \u03a9")  # \uXXXX → Ω（ギリシャ文字オメガ）
print("Unicode絵文字: \U0001f600")  # \UXXXXXXXX → スマイル絵文字
