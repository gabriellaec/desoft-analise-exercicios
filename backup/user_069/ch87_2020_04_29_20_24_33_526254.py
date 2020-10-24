import csv
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    valor = 0
    for i in conteudo:
        valor += i[1]*i[2]     
print(valor)