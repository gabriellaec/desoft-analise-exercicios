import csv
custo=0
with open  ('churras.txt') as arquivo:
    consumo=csv.reader(lista)
    for row in consumo:
        quant=float(row[1])
        preco=float(row[2])
        custo+=preco*quant
print (custo)

    