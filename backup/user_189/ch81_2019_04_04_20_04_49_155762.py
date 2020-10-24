def interseccao_valores(dic1,dic2):
    lista=[]
    for a in dic1.values():
        for b in dic2.values():
            if a==b:
                lista.append(a)
        return lista