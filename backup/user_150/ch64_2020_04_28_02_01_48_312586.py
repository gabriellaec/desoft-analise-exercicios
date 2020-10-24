def acha_bigramas(string):
    lista_bigramas = []
    i = 2
    g = 0
    l = 0
    while l < len(string)-1:
        while i <= len(string):
            bigramas = string[g:i]
            if bigramas not in lista_bigramas:
                lista_bigramas.append(bigramas)
            i += 1
            g += 1
        l += 1
    return lista_bigramas