with open('dados.csv','r') as CSV:
    conteudo = CSV.read()
    TSV = conteudo.replace(',', '\t')
with open ('dados.tsv', 'w') as TSV:
    write(TSV)