def interseccao_valores(dic1,dic2):
    lista=[]
    for t in dic1.values():
        if t in dic2.values():
            lista.append(t)
    return lista