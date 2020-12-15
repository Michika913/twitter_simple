#訂正情報以外からデマ情報を検出
#訂正情報と重複するものを抽出
#その他情報　test.binaryfile
#訂正情報　predicted.data.binaryfile
import pickle
import csv

file1 = open('predicted_data.binaryfile', 'rb')
word = pickle.load(file1)

file2 = open('test.binaryfile', 'rb')
all = pickle.load(file2)



list = []
for l in range(len(word)):
  S1 = set(word[l])
  for i in range(len(all)):
    S2 = set(all[i])

    if len(S1 & S2) >= (len(S1)* 0.4) :
      list.append([word[l], all[i]])
      with open("result.csv", "a", encoding="utf_8_sig", newline="") as files:
        print("訂正", word[l], ",", "デマ", all[i], file = files)


