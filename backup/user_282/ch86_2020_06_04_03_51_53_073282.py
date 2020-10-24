with open('dados.csv', 'r') as conteudo:
    csv = conteudo.read()

    with open('dados.tsv', 'w') as tsv:
        tsv.write("csv")