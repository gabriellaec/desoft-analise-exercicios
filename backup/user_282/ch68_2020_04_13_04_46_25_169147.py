def separa_trios(lista):
    trios = list()
    for i in range(0, len(lista), 3):
        trios.append(lista[i:i+3])
    return trios