with open('dados.csv','r') as arquivo:
    texto=csv.read()
t1=texto.split(',')
t2=('	'.join(t1))
with oepn('dados.tsv','w') as tsv:
    tsv.write(t2)
        