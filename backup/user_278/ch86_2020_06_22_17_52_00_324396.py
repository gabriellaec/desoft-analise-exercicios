with open ('dados.csv', 'r') as csv:
    conteudo = csv.read()
    conteudo2 = conteudo.replace(',', '\t')
    with open ('dados.tsv', 'w') as tsv:
        tsv.write(conteudo2)