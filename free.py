import requests
import sys
import MeCab
from time import sleep
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


# 解析対象テキストファイルを開く
with open('count_word.csv', newline='') as f:

# ファイルを読み込むo
    word_list = f.read().split("\n")

# Step3：名詞の出現頻度からTF-IDF/COS類似度を算出。テキスト情報のマッチ度を測る
def tfidf(word_list):
    docs = np.array(word_list)#Numpyの配列に変換する
    #単語を配列ベクトル化して、TF-IDFを計算する
    vecs = TfidfVectorizer(
                token_pattern=u'(?u)bw+b'#文字列長が 1 の単語を処理対象に含めることを意味します。
                ).fit_transform(docs)
    vecs = vecs.toarray()
    return vecs

def cossim(v1,v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))



vecs = tfidf(word_list)
print(cossim(vecs[1], vecs[0]))
