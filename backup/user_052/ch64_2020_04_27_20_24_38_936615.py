def acha_bigramas (texto):
    i = 0
    lista = []
    while i < len(texto)-1:
        a = texto[i]
        b = texto[i+1]
        if a+b not in lista:
            lista.append(a+b)
        i += 1
    return lista