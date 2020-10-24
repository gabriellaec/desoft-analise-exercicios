def mais_populoso (dic_estados):
    
    maior_pop = 0
    maior_estado = 0
    populoso = 0
    
    for k, dicinho in dic_estados.items(): 
        numeros = dicinho.values()
        for valor in numeros:
            populoso += valor
        
        if abs(populoso)  > maior_pop:
            maior_pop = populoso 
            maior_estado = k
            
    return maior_estado 