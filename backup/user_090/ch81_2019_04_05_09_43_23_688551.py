def interseccao_valores(a,b):
    lista=[]
    for x,y in a:
        if x in b:
            lista.append(x)
    return lista