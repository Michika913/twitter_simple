import MeCab
import pandas as pd

# datetime
import time
# 引数取得
import sys
from sys import argv
# 分かち書きのみ出力する設定にする

# m = MeCab.Tagger("-Owakati")

# 解析対象テキストファイルを開く
lines = pd.read_csv("データセット2.csv", usecols=[3, 4])
lines.to_csv("./train2.tsv", sep="\t", index=False, header=False)

# for line in open('result.txt', 'r'):
#     words = m.parse(line)
#     words = words.rstrip('\n')
#     print(words)
#
#
#
#
#
# #ファイル実行開始時刻を取得
# timestr = time.strftime('%Y%m%d-%H%M%S')
#
# #出力ファイル名
# out_file_name = "owakati.txt"
# with open(out_file_name, 'w') as f:
#     f.write(words)
