def separa_trios(lista):
    lista2 = []
    i = 0
    while i < len(lista):
        trios = lista[i:i+3]
        lista2.append(trios)
        i+=3
    return lista2