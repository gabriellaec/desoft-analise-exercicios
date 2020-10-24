import csv
with open('dados.csv', 'r') as arquivo_csv:
    read_csv = csv.reader(arquivo_csv)
    
    with open('dados.tsv', 'w') as arquivo_tsv:
        write_tsv = csv.writer(arquivo_tsv, delimiter = '	')
        
        for l in read_csv:
            write_tsv.writerow(l)
        