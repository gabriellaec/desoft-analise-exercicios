def conta_bigramas(lista):
    dicio = {}
    lista1 = []
    for a in range(0, len(lista)-1):
        lista1.append(lista[a]+lista[a+1])
    for n in lista1:
        dicio[n] = lista1.count(n)
    return dicio
                      
        
        