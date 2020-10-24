def interseccao_valores (d1,d2):
    lista=[]
    for k in d1.Keys():
        if k in d2.Keys():
            lista.append(k)
    return lista
            
            
    