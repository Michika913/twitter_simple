#分類器にかけるよう前処理
import pandas as pd

# 解析対象テキストファイルを開く
lines = pd.read_csv("test_tweet.csv", usecols=[0])
lines.to_csv("./test_tweet.tsv", sep="\t", index=False, header=False)
