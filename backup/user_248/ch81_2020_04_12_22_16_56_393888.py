def interseccao_valores(dic1,dic2):
    v=dic1.values
    v2=dic2.values
    lista=[]
    for k in v:
        for k in v2:
            lista.append(k)
    return lista