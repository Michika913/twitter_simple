#訂正情報以外からデマ情報を検出
#訂正情報と重複するものを抽出
#その他情報　test.binaryfile
#訂正情報　predicted.data.binaryfile
import pickle
import csv

file1 = open('predicted_tweet.binaryfile', 'rb')
words = pickle.load(file1)
word =[x[0] for x in words]
word2 =[p[1] for p in words]
#print (word2)
file2 = open('test.binaryfile', 'rb')
terms = pickle.load(file2)
term = [y[0] for y in terms]
term2 =[q[1] for q in terms]



list = []
for l in range(len(word)):
  S1 = set(word[l])
  correct = word2[l]
  for i in range(len(term)):
    S2 = set(term[i])
    rumor = term2[i]

    if len(S1 & S2) >= (len(S1)* 0.4) :
      list.append([word[l], term[i]])
      with open("test_result.csv", "a", encoding="utf_8_sig", newline="") as files:
        print("訂正", word[l], ",", "デマ", term[i], file = files)

      with open("false_rumor.csv", "a", encoding="utf_8_sig", newline="") as file1:
        print(term2[i], file = file1)


