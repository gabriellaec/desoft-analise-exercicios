with open('dados.csv', 'r') as csv:
    ler_csv=csv.read()
t1=texto.split(',')
t2=('	'.join(t1))
with open('dados.tsv', 'w') as tsv:
    tsv.write(t2)