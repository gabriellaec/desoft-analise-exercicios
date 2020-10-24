def separa_trios(lista):
    i=1
    while i < len(lista):
        oi = lista[i][i+1][i-1].split(",")
        i+=3
    return oi