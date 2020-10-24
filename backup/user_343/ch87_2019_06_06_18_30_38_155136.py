import csv
custo=0
with open('churras.txt') as lista:
    conteudo=csv.reader(lista)
    for i in conteudo:
        q=float(i[1])
        p=float(i[2])
        custo=q*p
        
print (custo)
    