def acha_bigramas(string):
    lista = []
    for i in range(len(string)-1):
        big = string[i] + string[i+1]
        lista.append(big)
    return lista