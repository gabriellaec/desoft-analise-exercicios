def bairro_mais_custoso(dici):
    
    dic = total_do_semestre_por_bairro(dici)
    
    lista_p = []
    
    for k,v in dic.items():
        
        lista_p.append(v)
        
    caro = max(lista_p)
    print(caro)
    
    for k,v in dic.items():
        
        dic[k] = caro
        
    return k