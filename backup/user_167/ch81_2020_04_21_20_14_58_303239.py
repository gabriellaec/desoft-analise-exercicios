def interseccao_valores (d1,d2):
    lista=[]
    for v in d1.values():
        if v in d2:
            lista.append(v)
    return lista
            
            
    