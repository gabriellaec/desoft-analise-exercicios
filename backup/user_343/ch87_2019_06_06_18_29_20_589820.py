import csv
with open("churras.txt", "r") as arquivo:
    conteudo=csv.reader(arquivo)
    for i in conteudo:
        q=float(i[1])
        p=float(i[2])
        c=q*p
        
print (c)
    