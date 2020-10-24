def interseccao_valores(d1,d2):
    lista=[]
    for v in d1:
        for t in d2:
            if d1[v] == d2[t]:
            	lista.append(d1[v])
    return lista