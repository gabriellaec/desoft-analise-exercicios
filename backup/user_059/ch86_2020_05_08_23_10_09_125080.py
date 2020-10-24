import csv
import tsv

with open('dados.csv') as arquivo:
    reader = csv.reader(arquivo, delimiter='	')