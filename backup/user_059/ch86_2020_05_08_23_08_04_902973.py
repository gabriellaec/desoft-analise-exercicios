import csv

with open('myfile.tsv') as tsvfile:
  reader = csv.reader(tsvfile, delimiter='	')
  for row in reader:
    print(row)