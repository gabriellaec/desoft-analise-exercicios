def separa_trios(lista):
    listan = []
    for i in range(0, len(lista), 3):
        a = lista[i:i+3]
        listan.append(a)
    return listan