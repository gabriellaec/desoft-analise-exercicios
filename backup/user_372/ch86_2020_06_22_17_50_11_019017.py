with open('dados.csv', 'r') as arquivo_csv:
    conteudo = arquivo_csv.read()
    conteudo.replace('.','\t')
    novo_conteudo = tsv.dumps(conteudo)
    with open('dados.tsv', 'w') as arquivo_tsv:
        arquivo_tsv.write(novo_conteudo)