with open('dados.csv', 'w') as arquivo_csv:
    conteudo_csv = arquivo_csv.read()
    tsv = conteudo_csv.replace(',', '\t')
    with open('dados.tsv', 'w') as arquivo_tsv:
        conteudo = arquivo_tsv.write(tsv)