with open('dados.csv', 'r') as arquivo_em_csv:
    conteudo_csv = arquivo_em_csv.read()

conteudo_tsv = conteudo_csv.replace(',', '\t')

with open('dados.tsv', 'w+') as arquivo_em_tsv:
    arquivo_em_tsv.write(conteudo_tsv)