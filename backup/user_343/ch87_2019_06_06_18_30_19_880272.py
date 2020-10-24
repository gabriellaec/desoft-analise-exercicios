import csv
custo=0
with open('churras.txt') as arquivo:
    conteudo=csv.reader(arquivo)
    for i in conteudo:
        q=float(i[1])
        p=float(i[2])
        custo=q*p
        
print (custo)
    