import pandas as pd
import MeCab
import csv
import json
import codecs
import collections


# 解析対象テキストファイルを開く
with open('predicted_data.csv', newline='') as f:

# ファイルを読み込むo
    sample_text = f.read().split("\n")

tokenizer = MeCab.Tagger('../opt/anaconda3/lib/python3.7/site-packages/Mecab/mecab-ipadic-neologd')
tokenizer.parse("")


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

    c = collections.Counter(keywords)
    print(c)
    print(keywords, file=codecs.open("count_word.txt","a"))

#, file=codecs.open("count_word.txt","w")
#  writer = csv.writer(files, lineterminator='\n')