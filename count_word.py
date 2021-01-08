#訂正情報(bertによる分類)の固有名詞・一般名詞・動詞を抽出
import pandas as pd
import MeCab
import csv
import json
import codecs



# 解析対象テキストファイルを開く
with open('delurl_tweet.csv', newline='') as f:

# ファイルを読み込むo
    sample_text = f.read().split("\n")

tokenizer = MeCab.Tagger('../opt/anaconda3/lib/python3.7/site-packages/Mecab/mecab-ipadic-neologd')
tokenizer.parse("")

all = []
for line in sample_text:
    keywords = []
    node = tokenizer.parseToNode(line)

    while node:
        if node.feature.split(",")[1] == "固有名詞":
            keywords.append(node.surface)
        elif node.feature.split(",")[1] == "一般":
            keywords.append(node.surface)
        elif node.feature.split(",")[0] == "動詞":
            keywords.append(node.feature.split(",")[6])

        node = node.next
    c = len(keywords)
    all.append((keywords, line))
    #csvに、抽出した形態素とその数を出力
    with open("predicted_tweet.csv", "a", encoding="utf_8_sig", newline="") as files:
        print(c, ",",  keywords, ",", line, file = files)

#pandasデータフレーム化
col_names = ['c{0:02d}'.format(i) for i in range(100)]
df = pd.read_csv('predicted_tweet.csv', encoding='utf_8_sig', names = col_names)
print(df["c00"].mean())

#pickleに保存する
import pickle
with open('predicted_tweet.binaryfile', 'wb') as web:

    pickle.dump(all, web)



#, file=codecs.open("count_word.txt","w")
#  writer = csv.writer(files, lineterminator='\n')
#df = pd.read_csv('count_word.txt')
#df.mean(axis='colums')
