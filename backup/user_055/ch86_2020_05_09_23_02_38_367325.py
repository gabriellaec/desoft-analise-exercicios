with open('dados.csv', 'w') as arquivo_csv:
    conteudo_csv = arquivo_csv.read()
    tsv = conteudo_csv.replace(',', '	')
    with open('dados.tsv', 'w') as arquivo_tsv:
        arquivo_tsv.write(tsv)