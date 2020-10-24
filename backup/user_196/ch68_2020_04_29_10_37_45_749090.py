def separa_trios(lista):
    i=0
    while i < len(lista):
        lista[i][i+1][i-1].split(",")
        i+=2
    return lista