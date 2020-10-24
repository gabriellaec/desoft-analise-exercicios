import csv
csv.writer(file('dados.tsv', 'w+'), delimiter='\t').writerows(csv.reader(open("dados.csv")))