import csv
import tsv

with open('dados.csv') as tsvfile:
    reader = tsv.reader(csvfile, delimiter='\t')