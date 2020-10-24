def interseccao_chaves(dic1,dic2):
    lista=[]
    for e in dic1.keys():
        if e not in lista:
        	lista.append(e)
    for i in dic2.keys():
        if i not in lista:
        	lista.append(i)
    
    
    return lista