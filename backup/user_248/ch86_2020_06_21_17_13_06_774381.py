with open('dados.csv','r') as arquivo:
    file=arquivo.read().replace(',',' ')
    with open('dados.tsv', 'w') as arquivo2:
        arquivo2.write(file)