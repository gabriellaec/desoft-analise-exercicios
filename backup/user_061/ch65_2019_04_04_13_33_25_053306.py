def acha_bigramas(string):
    lista = []
    i = 0
    while i < len(string)-1:
        bigrama = string[i]+string[i+1]
        if bigrama not in lista:
            lista.append(bigrama)
        i+=1
    return lista