with open('dados.csv', 'r') as arquivo_csv:
    conteudo = arquivo_csv.read()
arquivo_tsv = conteudo.replace(',', '\t')
with open('dados.tsv', 'w') as arquivo:
    arquivo.write(arquivo_tsv)
