def paoupg(lista):
    x="nada"
    for i in lista:
        if lista[i]/lista[i-1]==lista[i+1]/lista[i]:
            x="PG"
        elif lista[i]-lista[i-1]==lista[i+1]-lista[i]:
            x="PA"
        else:
            x="NA"
    return x

paoupg([1, 2, 3, 4, 5, 6, 7])