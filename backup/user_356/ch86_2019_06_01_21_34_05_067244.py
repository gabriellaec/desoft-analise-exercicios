with open('dados_csv.csv', 'r') as dados_csv:
    conteudo=dados_csv.read()
with open('dados_tsv.tsv','w') as dados_tsv:
    dadoso_tsv.write(conteudo)