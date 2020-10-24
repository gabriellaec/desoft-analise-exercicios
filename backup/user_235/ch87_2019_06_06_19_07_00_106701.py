import cvs
cost=0
with open ("churras.txt") as lista:
    consumo=cvs.reader(lista)
    for row in consumo:
        quantidade=float(row[1])
        preco=float(row[2])
        cost+=quantidade*preco
print(cost)
    