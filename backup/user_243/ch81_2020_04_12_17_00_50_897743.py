def interseccao_valores(dic1,dic2):
    lista=[]
    for k in dic1.values():
        lista.append(k)
    for k in dic2.values():
        lista.append(k)
    return lista