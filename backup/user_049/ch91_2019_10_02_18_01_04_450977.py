import csv

lista = []
with open('palavras.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')

    for linha in spamreader:
        lista.append(linha)

i=0
quantidade=0
while i < len(lista[0]):
    if lista[0][i][0] == 'a' or lista[0][i][0] == 'A':
        quantidade+=1
    i+=1

print(quantidade)
