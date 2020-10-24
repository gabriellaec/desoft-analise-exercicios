def acha_bigramas(string):
    lista = []
    i = 1
    while i < len(string):
        a = string[i]
        b = string[i - 1]
        c = b + a
        if c not in lista:
            lista.append(c)
        i += 1
    return lista