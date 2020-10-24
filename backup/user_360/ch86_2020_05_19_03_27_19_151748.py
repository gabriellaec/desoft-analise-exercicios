with open('dados.csv', 'r') as arq:
    cont = arq.read()
    troca = cont.replace(',', ' ')
    with open('dados.tsv', 'w') as arq2:
        r = arq2.write(troca)