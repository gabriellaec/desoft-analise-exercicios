def mais_populoso (dic_estados):
    
    maior_pop = 0
    maior_estado = 0
    
    for k, v in dic_estados.items: 
        numeros = v.values()
        populoso = sum(numeros)
        
        if numeros  > maior_pop:
            maior_pop = numeros 
            maior_estado = k
            
    return maior_estado 