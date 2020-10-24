with open('dados.csv','r') as csv:
    texto = csv.read()

t1 = texto.split(',')
t2 = t1.join('	')


with open('dados.tsv','w') as tsv:
    tsv.write(t2)