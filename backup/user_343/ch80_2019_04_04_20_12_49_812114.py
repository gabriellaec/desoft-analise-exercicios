def interseccao_chaves(dic1, dic2):
    lista=[]
    keys=dic1.keys()
    keys1=dic2.keys()
    for k in keys:
        lista.append(k)
    for e in keys1:
        lista.append(e)
    return lista
print (interseccao_chaves(dic1, dic2))    
                       
                       
                       
