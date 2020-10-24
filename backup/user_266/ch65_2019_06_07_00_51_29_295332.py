def acha_bigramas(string):
    lista = []
    i = 1
    while i < len(string):
        if string[i-1] + string[i] not in lista:
            lista.append(string[i-1] + string[i])
        i+=1
    return lista