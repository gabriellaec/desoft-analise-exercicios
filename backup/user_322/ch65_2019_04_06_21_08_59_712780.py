def acha_bigramas(n):
    lista = []
    lista2 = []
    for i in range(0,len(n)-1):
        lista.append(n[i]+n[i+1])
    for e in lista:
        if e not in lista2:
            lista2.append(e)
    return lista2