import csv

with open ('dados.csv') as entrada:
    texto=entrada.read()
t1=texto.split(',')
t2=t1.join('\t')

with open ('dados.tsv') as saida:
    saida.write(t2)

    
