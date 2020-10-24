def mais_populoso (dic_estados):     
    
    maior_populacao = 0        
    maior_estado = 0
    
    
    for estado, dic_interno in dic_estados.items():   # Aqui percorro as keys(estados) e values(dicionario com cidade e pop) do dic principal.
        pop = 0   # Crio uma variável para ir iterando com as soma das populações de cada cidade

        for valor in  dic_interno.values():   # Pra cada estado estou percorrendo os values de seu dic interno e somando, o que vai dar a pop de cada estado
            pop += valor                      #soma as pop pra cada estado
        
        if pop > maior_populacao:          #estabelece maior pop e estado com maior pop até aparecer um maior   
            maior_populacao = pop          
            maior_estado = estado
            
    return maior_estado