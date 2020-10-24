import csv
with open('dados.csv', 'r') as arquivo:
    conteudo = csv.reader(arquivo)
    with open('dados.tsv', 'w') as arquivo2:
        conteudo2 = csv.writer(arquivo2, delimiter = '\t')
        for l in conteudo:
            conteudo2.writerow(l)
            
        