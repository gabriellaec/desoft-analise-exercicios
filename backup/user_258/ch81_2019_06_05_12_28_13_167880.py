def interseccao_valores(dic1, dic2):
    lista_dic1 = []
    lista_dic2 = []
    for e in dic1.values():
        lista_dic1.append(e)
    for k in dic2.values():
        lista_dic2.append(k)
    lista_interseccao = []
    i = 0
    while i < len lista_dic1:
        lista_interseccao.append(lista_dic1[i], lista_dic2[i])
        i += 1
    return lista_interseccao