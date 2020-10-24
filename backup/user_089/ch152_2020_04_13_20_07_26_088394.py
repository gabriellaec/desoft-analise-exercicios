def verifica_preco(st,dic,cp):
    
    if st in dic:
          
        if dic[st] in cp:
        
            return cp[dic[st]]