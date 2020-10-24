def acha_bigramas(string):
    lista = []
    i = 1
    while i < len(string):
        bigrama = string[i-1]+string[i]
        if bigrama not in lista:
            lista.append(bigrama)
        i+=1
    return lista