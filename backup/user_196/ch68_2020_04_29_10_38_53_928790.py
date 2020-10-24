def separa_trios(lista):
    i=1
    while i < len(lista):
        lista[i][i+1][i-1].split(",")
        i+=2
    return lista