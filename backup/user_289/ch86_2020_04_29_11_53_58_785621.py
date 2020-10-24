with open('dados.csv', 'r') as arquivo_csv:
    conteudo_csv = arquivo_csv.read()
    arquivo_tsv = conteudo_csv.replace(',','\t')
with open('dados.tsv', 'a') as arquivo:
    arquivo.writelines(arquivo_tsv)