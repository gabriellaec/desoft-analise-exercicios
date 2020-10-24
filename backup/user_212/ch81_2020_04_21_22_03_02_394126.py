def interseccao_valores (dic1,dic2):
    lista=[]
    chaves=dic1.values()
    for v in chaves:
        if v in (dic2.values()):
            lista.append(v)
    return lista
        