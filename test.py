#デマ情報の検出
#訂正情報と重複するものを抽出
import pickle


file1 = open('test.binaryfile', 'rb')
word = pickle.load(file1)

file2 = open('predicted_data.binaryfile', 'rb')
all = pickle.load(file2)



list = []
for l in range(len(word)):
  S1 = set(word[l])
  for i in range(len(all)):
    S2 = set(all[i])

    if len(S1 & S2) >= 10:
      list.append([word[l], all[i]])
      with open("post-test.csv", "a", encoding="utf_8_sig", newline="") as files:
        print(word[l], ",", all[i], file = files)


