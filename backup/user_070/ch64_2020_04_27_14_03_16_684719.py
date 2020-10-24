def acha_bigramas(s):
    lista = []
    for i in range(len(s)-1):
        if s[i:i+2] not in lista:
            lista.append(s[i:i+2])
    return lista