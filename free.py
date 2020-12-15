#①訂正情報(bertによる分類)
# delurl_tweet1.csv
#count_word.pyで品詞抽出　ー固有名詞・一般名詞・動詞
#抽出結果をcount_word.csv
#pickleで保存したものがpredicted_dara.binaryfile

#②その他の情報(デマ情報を含む)
#test_tweet.csv
#free.py(これ)で品詞抽出
#抽出結果をtest.csv
#pickleで保存したものがtest.binaryfile

#③その他情報と訂正情報の重複を抽出
#test.pyで実行
#ある一定の割合で重複していたら訂正情報とともに出力　→デマ認定
#post-test.csvに出力



import pandas as pd
import MeCab
import csv
import json
import codecs



# 解析対象テキストファイルを開く
with open('test_tweet2.csv', newline='') as f:

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
    # csvに、抽出した形態素とその数を出力
    with open("test2.csv", "a", encoding="utf_8_sig", newline="") as files:
        print(c, ",",  keywords, file = files)


#pandasデータフレーム化
col_names = ['c{0:02d}'.format(i) for i in range(100)]
df = pd.read_csv('test2.csv', encoding='utf_8_sig', names = col_names)
print(df["c00"].mean())

#pickleに保存する
import pickle
with open('test2.binaryfile', 'wb') as web:
  pickle.dump(all, web)


#, file=codecs.open("count_word.txt","w")
#  writer = csv.writer(files, lineterminator='\n')
#df = pd.read_csv('count_word.txt')
#df.mean(axis='colums')
