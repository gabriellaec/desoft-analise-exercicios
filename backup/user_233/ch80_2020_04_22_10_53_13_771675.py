def interseccao_chaves(dict1, dict2):
    
    chaves = []
    
    for chave in dict1.keys():
        
        if chave in  dict2.keys(): chaves.append(chave)
            
    return chaves