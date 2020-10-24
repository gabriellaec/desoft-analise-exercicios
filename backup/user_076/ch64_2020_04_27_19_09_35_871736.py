def acha_bigramas (string):
    lista = []
    i=0
    while i+1 < len(string):
        bigrama = string[i] + string[i+1]
        if bigrama not in lista:
            lista.append(bigrama)
        i+=1
    return lista