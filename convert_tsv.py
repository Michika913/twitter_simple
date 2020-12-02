#分類器にかけるよう前処理
import pandas as pd

# 解析対象テキストファイルを開く
lines = pd.read_csv("データセット2.csv", usecols=[3, 4])
lines.to_csv("./train2.tsv", sep="\t", index=False, header=False)
