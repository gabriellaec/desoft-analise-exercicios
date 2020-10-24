def interseccao_chaves(dic1, dic2):
    
    lista = []
        
    for e in dic1.keys():
        
        for f in dic2.keys():
            
            if e == f:
                
                lista.append(e)
                
    return lista
    