def interseccao_chaves(x,y):
    lista=[]
    for e in x.keys():
        for i in y.keys():
            if i==e:
                lista.append(e)
        
    return lista
        
        
       
        