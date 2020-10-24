def interseccao_valores(dic1,dic2):
    lista=[]
    for i in dic1.values():
        for k in dic2.values():
            if i==k:
                lista.append(i)
    return lista