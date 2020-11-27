import pandas as pd
import MeCab
import csv
import json
import codecs



# 解析対象テキストファイルを開く
with open('predicted_data.csv', newline='') as f:

# ファイルを読み込む
    sample_text = f.read()


tokenizer = MeCab.Tagger("-Ochasen")
tokenizer.parse("")
node = tokenizer.parseToNode(sample_text)
keywords = []
for linr in sample_text:

    while node:
        if node.feature.split(",")[1] == u"固有名詞":
            keywords.append(node.surface)
        elif node.feature.split(",")[1] == u"一般名詞":
            keywords.append(node.surface)
        elif node.feature.split(",")[0] == u"動詞":
            keywords.append(node.feature.split(",")[6])


        node = node.next

    print(keywords, file=codecs.open("count_word.txt","w"))
