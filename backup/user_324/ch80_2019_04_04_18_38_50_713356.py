def interseccao_chaves(d, e):
    lista=[]
    for a in d:
        for b in e:
            if a==b:
             lista.append(a)
    return lista