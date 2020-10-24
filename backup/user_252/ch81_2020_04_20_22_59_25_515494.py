def interseccao_valores (d1, d2):
    lista=[]
    for i in d1.values():
        c=i
        for v in d2.values():
            b=v
            if c==b:
                lista.append(c)
                b=len(d2)
    return lista
 