def interseccao_valores(d1,d2):
    listaval = []
    lista_cor = []
    for v1 in d1.values():
        listaval.append(v1)
    for v2 in d2.values():
        listaval.append(v2)
    for i in listaval:
        if i in d1.values() and i in d2.values():
            if i not in lista_cor:
                lista_cor.append(i)
    return lista_cor