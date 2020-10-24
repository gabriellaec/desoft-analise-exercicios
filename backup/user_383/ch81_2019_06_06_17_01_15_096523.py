def interseccao_valores(dic1,dic2):
    lista_vazia=[]
    for k,v in dic1.items():
        if dic[k] in dic2:
            lista_vazia.append(dic1[k])
    return lista_vazia