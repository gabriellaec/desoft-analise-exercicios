with open('dados.csv', 'r') as arquivo:
    conteudo = arq.read()
    troca = conteudo.replace(',', ' ')
    with open('dados.tsv', 'w') as arquivo2:
        r = arquivo2.write(troca)