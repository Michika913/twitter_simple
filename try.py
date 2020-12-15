import pandas as pd
col_names = ['c{0:02d}'.format(i) for i in range(100)]
df = pd.read_csv('count_word.csv', encoding='utf_8_sig', names = col_names)
print(df["c00"].mean())

#pickleに保存する
import pickle
with open('predicted_data.binaryfile', 'wb') as web:
  pickle.dump(all, web)
