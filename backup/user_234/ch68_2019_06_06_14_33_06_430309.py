def separa_trios(lista):
    trios = []
    i=0
    b=3
    while i < len(lista):
        trio = lista[i:b]
        trios.append(trio)
        b+=3
        i+=3
    return trios