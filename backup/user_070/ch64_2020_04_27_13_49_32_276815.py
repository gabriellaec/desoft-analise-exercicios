def acha_bigramas(s):
    lista = []
    for i in range(len(s)-1):
        x = s[i] + s[i+1]
        if lista.find(x) == -1:
            lista += x
    return lista