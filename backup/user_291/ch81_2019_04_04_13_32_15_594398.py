def interseccao_chaves(dic1, dic2):
    
    lista = []
        
    for e in dic1.values():
        
        for f in dic2.values():
            
            if e == f:
                
                lista.append(e)
                
    return lista