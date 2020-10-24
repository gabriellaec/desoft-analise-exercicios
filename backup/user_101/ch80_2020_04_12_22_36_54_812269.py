def interseccao_chaves(dic1,dic2):
    lista1 = []
    lista2 = []
    for k in dic1:
        lista1.append(k)
    for k in dic2:
        lista2.append(k)
    l_final = []
    for e in lista1:
        if e in lista2:
            l_final.append(e)
    return l_final