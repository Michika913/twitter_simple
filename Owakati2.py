import MeCab
# datetime
import time
# 引数取得
import sys
from sys import argv
import csv

# 解析対象テキストファイルを開く
with open('訂正情報.csv', newline='') as f:

# ファイルを読み込む
    data = f.read()
text_data = []
# 分かち書きのみ出力する設定にする
for line in open('訂正情報.csv', 'r'):
    mecab = MeCab.Tagger("-Owakati")
    text = mecab.parse(data)
    mecab.parse('')
    text_data.append(text)

#出力ファイル名
    out_file_name = "owakati2.txt"
    with open(out_file_name, 'a') as file:
        print(text)

#出力結果：
# 一行目はうまく分かち書きできるけど
# 一行目が繰り返されるだけで二行目以降に移行しない謎