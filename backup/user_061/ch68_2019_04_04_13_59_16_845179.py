def acha_trio(lista):
    trios = []
    i = 0
    while i < len(lista)-1:
        trio = lista[i:(i+3)]
        trios.append(trio)
        i+=3
    return trios
    