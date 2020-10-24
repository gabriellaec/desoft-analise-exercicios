def acha_bigramas(string):
    lista = []
    for k in range (0, len(string)):
        if len(string[k:k+2])>1:
            lista.append(string[k:k+2])
    return lista