with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
um = conteudo.replace(',', ' ')
    with open('dados.tsv', 'w') as arquivo2:
        r = arquivo2.write(um)