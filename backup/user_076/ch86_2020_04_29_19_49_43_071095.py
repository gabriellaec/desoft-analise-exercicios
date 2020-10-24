with open('dados.csv','r') as arquivo_csv:
    conteúdo_csv = arquivo_csv.read()
    conteúdo_tsv = conteúdo_csv.replace(',','\t')

with open('dados.tsv','w') as arquivo_tsv:
    arquivo_tsv.write(conteúdo_tsv)
    