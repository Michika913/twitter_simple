import csv

tsv_files = ["teisei.log"]
for tsv_file in tsv_files:
    tsv_f = open("delurl_tweet2.tsv", 'r')
    tsv = csv.reader(tsv_f, delimiter='\t')
    with open("delurl_tweet2.csv", 'w', encoding='utf_8_sig', newline="") as csv_f:
        writer = csv.writer(csv_f, delimiter=",")
        for row in tsv:
            writer.writerow(row)
        csv_f.close()
    tsv_f.close()
