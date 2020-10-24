def interseccao_chaves(dic1,dic2):
    lista_dic1 = []
    lista_dic2 = []
    lista_resp = []
    for k in dic1:
        lista_dic1.append(k)
    for k in dic2:
        lista_dic2.append(k)
    for i in lista_dic1:
        if i in lista_dic2:
            lista_resp.append(i)
    return lista_resp
        