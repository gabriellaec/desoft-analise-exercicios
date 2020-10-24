def encontra_maximo(lista):
    lista1=[]
    for i in lista:
        for t in i:
            lista1.append(abs(t))
    return max(lista1)
        