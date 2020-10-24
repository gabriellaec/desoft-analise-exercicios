def interseccao_valores(a,b):
    lista=[]
    for x,y in a:
        if x,y in b:
            lista.append(x)
    return lista