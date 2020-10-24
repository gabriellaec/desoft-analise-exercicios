with open('dados.csv', 'r') as arquivo_csv:
    conteudo = arquivo_csv.read()
    conteudo.replace('.','	')
    novo_conteudo = conteudo
    with open('dados.tsv', 'w') as arquivo_tsv:
        arquivo_tsv.write(novo_conteudo)