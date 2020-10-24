import csv
custo=0
with open('churras.txt') as fdc:
    consumo=csv.reader(fdc)
    for x in consumo:
        quant=int(x[1])
        preco=float(x[2])
        custo+=quant*preco
print(custo)