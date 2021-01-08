import pandas as pd
import csv
import re

csvfile = "test_tweet.csv"

def main():
  df = pd.read_csv(csvfile, sep="\t", names=("text", "rabel"))
  df["text"] = df["text"].str.replace(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', '', regex=True)
  df["text"] = df["text"].str.replace(r'@[0-9a-zA-Z_]+', '', regex=True)
  df["text"] = df["text"].str.replace(' ', '', regex=True)

  df.to_csv("test_"+csvfile, sep="\t", index=False, header=False)


if __name__ == '__main__':
  main()