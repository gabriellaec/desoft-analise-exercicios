with open('dados.csv', 'r') as arquivo_em_csv:
    conteudo = arquivo_em_csv.read()

conteudo.replace(',', '\t')

with open('dados.tsv', 'w+') as arquivo_em_tsv:
    arquivo_em_tsv.write(conteudo)