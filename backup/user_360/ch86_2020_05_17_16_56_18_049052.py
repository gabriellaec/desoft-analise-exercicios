with open('dados.csv', 'r') as arq:
    file = arq.read().replace(',',' ')
    with open('dados.tsv', 'x') as arq2:
        arq2.write(file)