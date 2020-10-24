import csv
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    valor = 0
    for i in conteudo:
        l = i.split(',')
        for i in l:
            print (i)
        #valor += float(i[1])*float(i[2]) 
        print(l)
print(valor)