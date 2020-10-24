def separa_trios(lista):
    trios = []
    i = 0
    while i < len(lista):
        trios.append(lista[i:i+3])
        i += 3
    if len(lista) % 3 != 0:
        trios.append(lista[i-3:])
    return trios