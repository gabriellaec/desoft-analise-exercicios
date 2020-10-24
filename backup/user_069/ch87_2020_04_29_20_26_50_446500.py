import csv
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    valor = 0
    for i in conteudo:
        #valor += float(i[1])*float(i[2]) 
        print(i[1])
        print(i[2])
print(valor)