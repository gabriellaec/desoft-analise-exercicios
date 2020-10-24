with open('dados.csv','r') as csv:
    texto = csv.read()


t2 = '	'.join(texto)


with open('dados.tsv','w') as tsv:
    tsv.write(t2)