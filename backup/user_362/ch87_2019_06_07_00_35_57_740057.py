import csv
custo = 0
with open ("churras.txt") as listas:
    consumo=cvs.reader(lista)
    for row in consumo:
        quant=float(row[1])
        preco=float(row[2])
        custo+=quant*preco
print (custo)