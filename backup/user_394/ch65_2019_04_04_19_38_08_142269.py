def acha_bigramas (texto):
    lista = []
    for e in texto:
        if e in lista:
            lista[e] = lista[e-1] + 1
        else:
            lista[e] = lista[e-1]