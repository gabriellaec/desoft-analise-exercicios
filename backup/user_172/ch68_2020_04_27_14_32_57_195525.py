def separa_trios(lista):
    lista2 = []
    i=0
    while i < len(lista)+2:
        lista2.append([lista[i], lista[i+1], lista[i+2]])
        i+=3
    return lista2