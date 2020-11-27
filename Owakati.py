import MeCab
import pandas as pd
import csv

# datetime
import time
# 引数取得
import sys
from sys import argv
# 分かち書きのみ出力する設定にする

m = MeCab.Tagger("-Owakati")

# 解析対象テキストファイルを開く
for line in open('predicted_data.csv', 'r'):
     s =[]
     words = m.parse(line)
     words = words.rstrip('\n')
     print(words)


     with open('流言訂正わかち.csv', 'a', newline='', encoding='utf_8_sig') as f:
          writer = csv.writer(f, lineterminator='\n')
          writer.writerows(words)
     pass

#出力結果：
#ターミナルにはうまく分かち書きが出力される
# csvファイルだと一文字ずつ改行したものが出力されてしまう
