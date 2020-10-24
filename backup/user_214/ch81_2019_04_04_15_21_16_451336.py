def interseccao_valores(dic1, dic2):
    interseccao=[]
    valores = dic2.values()
    lista_valores = []
    for a in valores:
        lista_valores.append(a)
    for u in dic1:
        if dic1[u] in lista_valores:
            interseccao.append(dic1[u])
    return interseccao