import csv
with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    for i in conteudo:
        print(i)
