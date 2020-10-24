with open('dados.csv','r') as arquivo:
    arq=arquivo.read().replace(',',' ')
    with open('dados.tsv', 'w') as arquivo2:
        arquivo2.write(arq)