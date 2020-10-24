with open('dados.tsv', 'r') as arquivo:
    with open('dados.csv', 'r') as arquivo:
        conteudo = arquivo.read()
        conteudo2 = conteudo.replace(',','\t')
    



