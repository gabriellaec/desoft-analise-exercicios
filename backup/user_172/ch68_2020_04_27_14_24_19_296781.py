def separa_trios(lista):
    lista2 = []
    i=0
    while i < len(lista):
        x = ', '.join([lista[i], lista[i+1], lista[i+2]])
        lista2.append(x)
        i+=3
    return lista2