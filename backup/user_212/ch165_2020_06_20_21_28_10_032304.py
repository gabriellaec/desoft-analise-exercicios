def mais_populoso (dic_estados):
    
    maior_pop = 0
    maior_estado = 0
    populoso = 0
    
    for k, dicinho in dic_estados.items(): 
        numeros = dicinho.values()
        for valor in numero:
            populoso += valor
        
        if populoso  > maior_pop:
            maior_pop = numeros 
            maior_estado = k
            
    return maior_estado 