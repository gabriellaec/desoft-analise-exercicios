def acha_bigramas(s):
    lista=list(s)
    lista_bi = []
    for i in range (len(lista)-1):
        bi = lista[i] + lista[i+1]
        if bi not in lista_bi:
            lista_bi.append(bi)
    return lista_bi