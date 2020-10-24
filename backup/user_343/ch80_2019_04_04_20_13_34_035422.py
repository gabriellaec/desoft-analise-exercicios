def interseccao_chaves(dic1, dic2):
    lista=[]
    
    for k in dic1.keys():
        lista.append(k)
    for e in dic2.keys():
        lista.append(e)
    return lista
print (interseccao_chaves(dic1, dic2))    
                       
                       
                       
