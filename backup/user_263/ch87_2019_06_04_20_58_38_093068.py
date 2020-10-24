import csv

with open('churras.txt','r') as arquivo:
    conteudo = csv.reader(arquivo)
    soma = 0
    for row in conteudo:
        soma += int(row[1])*float(row[2])
        
    print(soma)