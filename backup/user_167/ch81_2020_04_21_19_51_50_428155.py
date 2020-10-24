def interseccao_valores (d1,d2):
    lista=[]
    for k,v in d1.items():
        if k in d2.Keys():
            lista.append(k)
    return lista
            
            
    