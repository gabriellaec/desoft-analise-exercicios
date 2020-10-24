def interseccao_valores(dic1, dic2):
    
    lista2=[]
    for k in dic1.values():
        
        for v in dic2.values():
    
            if k==v:
                lista2.append(v) 
                
    return lista2