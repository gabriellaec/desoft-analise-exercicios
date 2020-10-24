import csv

with open('dados.csv', 'r') as arquivo_csv, open('dados.tsv','w') as arquivo_tsv:
    arquivo_csv = csv.reader(arquivo_csv)
    arquivo_tsv = tsv.writer(arquivo_tsv, delimiter=' ')
    for row in arquivo_csv:
        arquivo_tsv.writerow(row)