def acha_bigramas(n):
    i = 0
    lista_bigramas = []
    while i < (len(n) - 1):
        bigrama = n[i] + n[i+1]
        if bigrama not in lista_bigramas:
            lista_bigramas.append(n[i] + n[i+1])
        i += 1
    return lista_bigramas