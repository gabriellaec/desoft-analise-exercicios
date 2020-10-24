def interseccao_valores(dic1,dic2):
    lista=[]
    for a in dic1:
        if a in dic2:
            lista.append(a)
    return lista