import csv
total=0
with open('churras.txt') as lista:
    consumo=csv.reader(lista)
    for row in consumo:
        quant=float(row[1])
        preco=float(row[2])
        total+=(quant*preco)
print(total)