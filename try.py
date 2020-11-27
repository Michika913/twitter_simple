import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pandas as pd
import MeCab
import csv
import matplotlib
import json

mecab = MeCab.Tagger('-Ochasen')

sample_text = '今日はよく晴れています。'
node = mecab.parseToNode(sample_text)

while node:
    word = node.surface
    pos = node.feature.split(",")[1]

    if pos == '名詞':
        word = node.surface
        print('{0}'.format(word))




    node = node.next
