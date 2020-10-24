def encontra_maximo(x):
    maior = x[0][0]
    lista = []
    for i in x:
        for j in i:
            lista.append(j)
    for k in lista:
        if k > maior:
            maior = k
    return maior
            
            