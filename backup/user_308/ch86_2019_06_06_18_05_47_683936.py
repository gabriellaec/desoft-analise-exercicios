import csv

with open ('dados.csv') as entrada:
    texto=entrada.read()
t1=texto.split(',')
t2=('	'.join(t1))

with open ('dados.tsv','w') as saida:
    saida.write(t2)

    
