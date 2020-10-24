def acha_bigramas(palavra):
    lista_bigramas = []
    i = 0
    while i < len(palavra) - 1:
        p = (palavra[i] + palavra[i+1])
        if p not in lista_bigramas:
            lista_bigramas.append(p)
        i += 1
    return lista_bigramas