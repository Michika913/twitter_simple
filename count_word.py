import pandas as pd
import MeCab
import csv
import json
import codecs



# 解析対象テキストファイルを開く
with open('predicted_data.csv', newline='') as f:

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
    all.append([c, keywords])
    with open("count_word.csv", "a", encoding="utf_8_sig", newline="") as files:
        print(c, ",",  keywords, file = files)


col_names = ['c{0:02d}'.format(i) for i in range(100)]
df = pd.read_csv('count_word.csv', encoding='utf_8_sig', names = col_names)
print(df["c00"].mean())

#pickleに保存する
import pickle
with open('predicted_data.binaryfile', 'wb') as web:
  pickle.dump(all, web)


#, file=codecs.open("count_word.txt","w")
#  writer = csv.writer(files, lineterminator='\n')
#df = pd.read_csv('count_word.txt')
#df.mean(axis='colums')
