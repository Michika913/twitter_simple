#訂正情報
# predicted_data.csv
#test.pyで品詞抽出
#抽出結果をcount_word.csv
#pickleで保存したものがpredicted_dara.binarufile

#その他の情報
#pre-test.csv
#free.py(これ)で品詞抽出
#抽出結果をtest.csv
#pickleで保存したものがtest.binaryfile

#デマ情報と訂正情報の重複を抽出
#test.pyで実行
#平均個数以上(まだ決まっていない)重複してたらデマ認定
#post-test.csvに出力



import pandas as pd
import MeCab
import csv
import json
import codecs



# 解析対象テキストファイルを開く
with open('pre-test.csv', newline='') as f:

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
    all.append(keywords)
    with open("test.csv", "a", encoding="utf_8_sig", newline="") as files:
        print(c, ",",  keywords, file = files)


col_names = ['c{0:02d}'.format(i) for i in range(100)]
df = pd.read_csv('test.csv', encoding='utf_8_sig', names = col_names)
print(df["c00"].mean())

#pickleに保存する
import pickle
with open('test.binaryfile', 'wb') as web:
  pickle.dump(all, web)


#, file=codecs.open("count_word.txt","w")
#  writer = csv.writer(files, lineterminator='\n')
#df = pd.read_csv('count_word.txt')
#df.mean(axis='colums')
