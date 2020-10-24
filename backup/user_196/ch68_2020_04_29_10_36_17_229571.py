def separa_trios(lista):
    for i in lista:
        lista[i][i+1][i-1].split(",")
    return lista