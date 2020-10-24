    import csv
with open('dados.csv','r') as csv_file, open('dados.tsv', 'w') as tsv_file:
    csv_file, tsv_file = csv.reader(csv_file), csv.writer(tsv_file, delimiter='\t')
    for linha in csv_file:
        tsv_file.writerow(linha)