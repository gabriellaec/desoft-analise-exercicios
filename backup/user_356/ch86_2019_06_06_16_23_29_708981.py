with open('dados.csv', 'r') as dados_csv:
    conteudo=dados_csv.read()
with open('dados.tsv','w') as dados_tsv:
    dados_tsv.write(conteudo)