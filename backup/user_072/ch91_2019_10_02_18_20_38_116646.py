import csv

lista = []
listan=[]

with open('palavras.txt', newline='') as file:
    spamreader = csv.reader(file, delimiter=',')
    for linha in spamreader:
        lista.append(linha)

i=0
while i<len(lista):
    if lista[i][0]=='a' or lista[i][0]=='A':
        listan.append(lista[i])
    i+=1
print(len(listan))
            