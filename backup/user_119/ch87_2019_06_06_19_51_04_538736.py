with open ("churras.txt") as itens:
    lista = csv.reader(itens)
    for c in lista:
        q = float(c[1])
        p = float(c[2])
        custo += p*q
print (custo)