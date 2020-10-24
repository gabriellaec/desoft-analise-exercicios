def acha_bigramas (string):
    lista = []
    for i in range(len(string)-1):
        bigrama = string[i] + string[i + 1]
        if not bigrama in lista:
            lista.append(bigrama)
    return lista
    