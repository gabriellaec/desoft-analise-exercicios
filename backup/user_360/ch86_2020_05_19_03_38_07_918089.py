with open('dados.csv', 'r') as arquivo:
    conteudo = arquivo.read()
    switch = conteudo.replace(',', '')
    with open('dados.tsv', 'r') as arquivo2:
        x = arquivo2.write(switch)
        