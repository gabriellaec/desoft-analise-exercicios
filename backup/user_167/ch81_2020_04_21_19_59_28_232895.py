def interseccao_valores (d1,d2):
    lista=[]
    for k in d1.keys():
        if k in d2.keys():
            lista.append(k)
    return lista
            
            
    