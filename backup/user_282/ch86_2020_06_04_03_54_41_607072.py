import csv

csv.writer(open('dados.tsv', 'w+'), delimiter='\t').writerows(csv.reader(open("dados.csv")))
