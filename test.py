"""
c = 10
keyword = ["もじ"]

[[c, keyword]
[c, keyword]
[c, keyword]
[c, keyword]
[c, keyword]
[c, keyword]]

all = []

c = 10
keyword = ["もじ"]
all.appned([c, keyword])

pickle.dump( all   )

===========================
よみとったほう

pickle.load( all )

for i in range(1000):
  for t in all: #ツイート数くりかえす
    keyword = t[1]
"""
import pandas as pd
import pickle

with open('predicted_data.binaryfile', 'rb') as f:
  print(pickle.load(f))
keyword1 = ["あ", "い", "う", "さ"]
keyword2 = ["あ", "か", "さ"]

"デマを否定するのって難しくて、必死になって否定するなんて益々あやしい、って言われてしまう。ワクチンの話しとかと一緒。"

print(len( set(keyword1) & set(keyword2)) )

