import csv
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    valor = 0
    for i in conteudo:
        l = i.split(',')
        valor += float(l[1])*float(l[2]) 
print(valor)