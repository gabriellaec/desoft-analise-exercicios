def interseccao_chaves(dic1,dic2):
    
    lista=[]

    for i in dic1.values():
        for j in dic2.values():
            if(i==j):
                lista.append(j)
    
    return lista