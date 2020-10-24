def interseccao_valores(a,b):
    lista=[]
    for x in a.items:
        if x in b.items:
            lista.append(x)
    return lista