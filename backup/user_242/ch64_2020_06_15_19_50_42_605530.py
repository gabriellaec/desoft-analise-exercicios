def acha_bigramas(string):
    lista_bigramas = []
    for i in range(2, len(string)+1):
        x = string[i-2:i]
        if x not in lista_bigramas:
            lista_bigramas.append(x)
    return lista_bigramas