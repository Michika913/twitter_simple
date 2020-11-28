import pandas as pd
import csv
df = pd.read_csv('count_word.txt')
df.mean(axis='colums')