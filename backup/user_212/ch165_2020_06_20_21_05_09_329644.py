def mais_populoso (dic_estados):
    
    maior_pop = 0
    maior_estado = 0
    
    for k in dic_estados: 
        numeros = dic_estados[k].values()
        populoso = sum(numeros)
        
        if numeros  > maior_pop:
            maior_pop = numeros 
            maior_estado = k
            
    return maior_estado 