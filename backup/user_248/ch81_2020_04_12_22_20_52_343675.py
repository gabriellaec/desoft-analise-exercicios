def interseccao_valores(dic1,dic2):
    v=dic1.values()
    v2=dic2.values()
    lista=[]
    for i in v:
        if i in v2:
            lista.append(i)
    return lista