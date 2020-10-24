def acha_bigramas(texto):
    lista=[]
    for i in range(len(texto)-1):
        if texto[i]+texto[i+1] not in lista:
            lista.append(texto[i]+texto[i+1])
    return lista
    