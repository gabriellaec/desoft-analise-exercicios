def acha_bigramas(lista):
    lista_bigramas= []
    i= 0
    while i < len(lista)-1:
        lista_bigramas.append(lista[i]+lista[i+1])
        i= i + 1
    return lista_bigramas