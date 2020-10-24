with open('dados.csv', 'r') as em_csv:
    conteudo_csv = em_csv.read()
    
conteudo_tsv = conteudo_csv.replace(',', '	')

with open('dados.tsv', 'w+') as em_tsv:
    em_tsv.write(conteudo_tsv)