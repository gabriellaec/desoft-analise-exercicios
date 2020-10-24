with open('dados.csv', 'r') as dadoscsv:
    csv = dadoscsv.read()
    
tsv = csv.replace(',','\t')
