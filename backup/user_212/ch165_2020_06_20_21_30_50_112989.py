def mais_populoso (dic_estados):
    
    maior_pop = 0
    maior_estado = 0
    
    
    for k, dicinho in dic_estados.items():
        populoso = 0
        
        numeros = dicinho.values()
        for valor in numeros:
            populoso += valor
        
        if populoso > maior_pop:
            maior_pop = populoso 
            maior_estado = k
            
    return maior_estado 