def interseccao_valores(dic1, dic2):
    lista_dic1 = []
    lista_dic2 = []
    for e in dic1.values():
        lista_dic1.append(e)
    for k in dic2.values():
        lista_dic2.append(k)
    lista_interseccao = []
    for m in range(0, len(lista_dic1)):
        for n in range(0, len(lista_dic2)):
            if lista_dic1[m] == lista_dic2[n]:
                lista_interseccao.append(lista_dic1[m])
    return lista_interseccao