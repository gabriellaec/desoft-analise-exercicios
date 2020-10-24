def interseccao_valores (d1, d2):
    lista=[]
    for i in d1.valores():
        c=i
        for v in d2.valores():
            b=v
            if c==b:
                lista.append(c)
                b=len(d2)
    return lista
 