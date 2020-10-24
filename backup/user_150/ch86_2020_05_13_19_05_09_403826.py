with open('dados.csv', 'r') as arquivo:
    leitura = arquivo.read().replace(',', '\t')
    with open('dados.tsv','w') as arquivo2:
        arquivo2.write(leitura)