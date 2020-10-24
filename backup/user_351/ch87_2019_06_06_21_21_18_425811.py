import csv
custo = 0
with open ("churras.txt") as lista:
    consumo = csv.reader(lista)
    for row in consumo:
        quantidade = float(row[1])
        preco = float(row[2])
        custo+= quantidade + preco
print(custo)