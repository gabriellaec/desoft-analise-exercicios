def interseccao_valores(dic1, dic2):
    lista1 = []
    lista2 = []
    for v in dic1.value():
        lista1.append(v)
    for v in dic2.value():
        lista2.append(v)
    l_final = []
    for e in lista1:
        if e in lista2:
            l_final.append(e)
    return l_final