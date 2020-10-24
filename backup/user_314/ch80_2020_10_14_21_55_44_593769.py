def interseccao_chaves(dic1,dic2):
    
    lista=[]

    for i in dic1.keys():
        for j in dic2.keys():
            if(i==j):
                lista.append(j)
    
    return lista