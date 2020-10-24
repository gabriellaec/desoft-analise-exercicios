def separa_trios(lista):
    trios = []
    i = 0
    while i + 3 < len(lista):
        trios.append(lista[i:i+3])
        i += 3
    if len(lista) != i:
        trios.append(lista[i:])
    return trios