with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    switch = conteudo.replace(',', ' ')
    with open('dados.tsv', 'x') as arquivo2:
        x = arquivo2.write(switch)
        