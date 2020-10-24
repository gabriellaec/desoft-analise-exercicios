with open('dados.csv', 'r') as csv:
    texto=csv.read()
t1=texto.split()
t2=('	'.join(t1))
with open('dados.tsv', 'w') as tsv:
    tsv.write(t2)