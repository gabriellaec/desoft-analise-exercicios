def acha_bigramas(s):
    lista=list(s)
    lista_bi = []
    i = 0
    while i < (len(lista)-1):
        bi = lista[i] + lista[i+1]
        lista_bi.append(bi)
    return lista_bi