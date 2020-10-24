def acha_bigramas(s):
    lista = []
    for i in range(len(s)-1):
        x = s[i] + s[i+1]
        if x not in lista:
            lista += x
    return lista